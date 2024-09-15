import os
import openai
import subprocess

# Function to get the number of iterations from the user
def get_iterations():
    return int(input("How many improvements would you like to do? "))

# Function to write the content to the file
def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Function to read from a file
def read_from_file(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    else:
        return ""

# Function to commit and push changes to GitHub
def update_repo():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update content"])
    subprocess.run(["git", "push"])

# Function to call the API and get feedback on the content
def get_api_feedback(content, conversation, improvement_request):
    # Initialize the OpenAI API client
    client = openai.OpenAI()

    # Add the content (e.g., equation or subject matter) to the conversation
    conversation.append({"role": "user", "content": f"{content}"})

    # Send the conversation to the API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation
    )

    # Extract the feedback from the API response
    feedback = response.choices[0].message.content

    # Append the API feedback to the conversation
    conversation.append({"role": "assistant", "content": feedback})

    # Now send the feedback back to the API and ask for an improved content
    conversation.append({"role": "user", "content": f"{improvement_request}"})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation
    )

    # Extract the new content from the API response
    new_content = response.choices[0].message.content

    # Append this new content to the conversation and return it
    conversation.append({"role": "assistant", "content": new_content})

    return new_content, conversation

# Main function to run the loop
def main():
    # Load the context, professor message, and improvement request from .txt files
    content = read_from_file("content.txt")
    professor_message = read_from_file("professor_message.txt")
    improvement_request = read_from_file("improvement_request.txt")
    
    # Check if all files are present and valid
    if not content:
        print("No content found in 'content.txt'. Please provide the initial content (e.g., equation, biology problem, etc.).")
        content = input("Enter the initial content: ")
        write_to_file("content.txt", content)

    if not professor_message:
        print("No professor message found in 'professor_message.txt'. Please provide the initial professor message.")
        professor_message = input("Enter the professor message: ")
        write_to_file("professor_message.txt", professor_message)

    if not improvement_request:
        print("No improvement request found in 'improvement_request.txt'. Please provide the improvement request (e.g., ask for novel insight or improvements).")
        improvement_request = input("Enter the improvement request: ")
        write_to_file("improvement_request.txt", improvement_request)

    # Initialize an empty conversation
    conversation = []

    # Start with the professor message, asking the AI to critique the equation
    conversation.append({"role": "user", "content": professor_message})

    # Get the number of loops from the user
    loops = get_iterations()

    for _ in range(loops):
        # Send the content to the API and get feedback
        new_content, conversation = get_api_feedback(content, conversation, improvement_request)

        # Update the content file with the new content
        write_to_file("content.txt", new_content)

        # Update the GitHub repository with the new content
        update_repo()

        print(f"Content updated! New content:\n{new_content}")

if __name__ == "__main__":
    main()
