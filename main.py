import os
import openai
import subprocess

# Function to get the number of iterations from the user
def get_iterations():
    return int(input("How many loops would you like to do? "))

# Function to write the equation to the file
def write_equation_to_file(equation):
    with open("equation.txt", "w") as file:
        file.write(equation)

# Function to read the equation from the file
def read_equation_from_file():
    if os.path.exists("equation.txt"):
        with open("equation.txt", "r") as file:
            return file.read()
    else:
        return ""

# Function to commit and push changes to GitHub
def update_repo():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Update equation"])
    subprocess.run(["git", "push"])

# Function to call the API and get feedback on the equation
def get_api_feedback(equation, conversation):
    # Initialize the OpenAI API client
    client = openai.OpenAI()

    # Add the equation to the conversation
    conversation.append({"role": "user", "content": f"I suck at physics, I just wrote this equation:\n\n{equation}"})

    # Send the conversation to the API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation
    )

    # Extract the feedback from the API response
    feedback = response.choices[0].message.content

    # Append the API feedback to the conversation
    conversation.append({"role": "assistant", "content": feedback})

    # Now send the feedback back to the API and ask for an improved equation
    conversation.append({"role": "user", "content": "Based on your feedback, improve the equation and address all points. We are aiming for winning a Nobel here, so the equation needs to be novel. Reply only with the equation."})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=conversation
    )

    # Extract the new equation from the API response
    new_equation = response.choices[0].message.content

    # Append this new equation to the conversation and return it
    conversation.append({"role": "assistant", "content": new_equation})

    return new_equation, conversation

# Main function to run the loop
def main():
    # Read the current equation from file, or set to a default if it doesn't exist
    equation = read_equation_from_file()
    
    if not equation:
        print("No equation found in 'equation.txt'. Please provide an initial equation.")
        equation = input("Enter the initial equation: ")
        write_equation_to_file(equation)

    # Initialize an empty conversation
    conversation = []

    # Get the number of loops from the user
    loops = get_iterations()

    for _ in range(loops):
        # Read the current equation from file
        equation = read_equation_from_file()

        # Send the equation to the API and get feedback
        new_equation, conversation = get_api_feedback(equation, conversation)

        # Update the equation file with the new equation
        write_equation_to_file(new_equation)

        # Update the GitHub repository with the new equation
        update_repo()

        print(f"Equation updated! New equation:\n{new_equation}")

if __name__ == "__main__":
    main()
