### **Einstein-in-a-Box**

Welcome to **Einstein-in-a-Box**, an automated iterative content refinement tool that aims to push the boundaries of innovation in any field of study. Whether you’re working on physics equations, biological models, or complex mathematical theorems, this script sends your input to an AI for harsh, professor-like critique, and then iteratively refines it based on feedback.

---

### **How It Works**

1. **Initialization**:
   - The script reads the current content from a file (`content.txt`), along with an initial message (`professor_message.txt`) that sets the tone for feedback, and an improvement request (`improvement_request.txt`) that tells the AI how to enhance the content.
   - If any of these files are empty or missing, you'll be prompted to provide the required information.

2. **AI Feedback Loop**:
   - The content (e.g., equation, problem, model) is sent to the AI, which provides critical feedback as if it were a frustrated professor.
   - Based on this feedback, the AI refines the content to make it more novel, innovative, or corrected.
   - The improved content is saved back to `content.txt` and updated in the repository.

3. **GitHub Update**:
   - After each iteration, the updated content is committed and pushed to your GitHub repository automatically.

4. **Repeat**:
   - The loop runs for the number of iterations specified by the user.
   - Each cycle leads to a progressively refined version of the content.

---

### **Getting Started**

#### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/einstein-in-a-box.git
cd einstein-in-a-box
```

#### **2. Set Up Your Environment**

- Ensure you have Python installed.
- Install the required libraries (e.g., `openai`):
  
```bash
pip install openai
```

#### **3. Prepare Your Files**

Create the following three text files in the root of your repository:

1. **`content.txt`**: This file contains the initial content (e.g., a physics equation or any other problem). Example:
   ```txt
   \[ \left( \hat{H}_\mathrm{grav} + \hat{H}_\mathrm{matter} + \frac{\alpha}{L_\mathrm{P}^2} \int d^3x \sqrt{g} \, \hat{R}_{\mu\nu} \hat{T}^{\mu\nu} \right) \Psi[g_{\mu\nu}, \phi] = 0 \]
   ```

2. **`professor_message.txt`**: This file contains the message asking the AI to critique the content harshly. Example:
   ```txt
   I suck at physics, I just wrote this equation:

   \[ \left( \hat{H}_\mathrm{grav} + \hat{H}_\mathrm{matter} + \frac{\alpha}{L_\mathrm{P}^2} \int d^3x \sqrt{g} \, \hat{R}_{\mu\nu} \hat{T}^{\mu\nu} \right) \Psi[g_{\mu\nu}, \phi] = 0 \]

   Please bash on it, be very mean to it, as if you were a PhD professor who is frustrated with how bad I am in physics.
   ```

3. **`improvement_request.txt`**: This file tells the AI to improve the content after the critique. Example:
   ```txt
   Based on your feedback, improve the equation and address all points. We are aiming for a Nobel-worthy discovery, so please ensure the equation is novel and addresses cutting-edge topics in physics. Reply only with the equation.
   ```

#### **4. Configure API Key**

You'll need an OpenAI API key to use the script. For security reasons, **do not hardcode** your API key directly into the script if you're pushing to a public repository. Use environment variables or a secret management tool. If you're not sure how, check OpenAI’s [API documentation](https://beta.openai.com/docs/) for help.

**Warning**: If you're hardcoding your key for personal use, be sure to remove the auto GitHub push feature or use a private repository to avoid leaking the key.

#### **5. Run the Script**

Simply execute the script:

```bash
python main.py
```

#### **6. Enter the Number of Iterations**

The script will prompt you to enter the number of iterations (loops) you'd like the content to go through. Each iteration involves getting feedback, refining the content, and pushing updates to your GitHub repo.

---

### **Usage Example**

1. **Initial Content**:
   When you run the script for the first time, it will read the initial content from `content.txt`. If the file is empty, you'll be asked to provide the content manually.

2. **Iterate**:
   The AI will critique the content, then improve it based on your `improvement_request.txt`. After each iteration, the script updates `content.txt` with the new version and pushes changes to your GitHub repository.

---

### **Flexible for Any Field**

This tool isn't limited to physics. You can use it for:

- **Mathematics**: Provide complex equations or theorems.
- **Biology**: Test scientific models or hypotheses.
- **Chemistry**: Refine chemical equations or molecular theories.
- **Engineering**: Improve designs or calculations.

By changing the content and the improvement request, this tool can adapt to any field where iterative refinement is needed.

---

### **Contributing**

Feel free to contribute by opening issues or submitting pull requests. Suggestions for improvements are welcome!

---

### **License**

This project is licensed under the MIT License.

---

### **Disclaimer**

This script is a fun, experimental project! The content produced may not be scientifically valid and should be treated as such unless verified by an expert in the field.

---

Now, fire up the loop and start refining your equations, models, or theorems. Who knows? You might just create the next revolutionary discovery! 😊

---

### Final Note

Remember to adjust the contents of `content.txt`, `professor_message.txt`, and `improvement_request.txt` for any field of study you want to work on. This flexibility allows you to use the same script for various subjects, making it an incredibly versatile tool for innovation!

