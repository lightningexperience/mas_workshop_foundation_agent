<h1>Foundation Agent (Stage 0)</h1>

<p>
  A minimal LLM-powered chatbot using Groq’s ChatCompletions API and Streamlit.
  This agent is intentionally simple: no memory, no grounding, no frameworks.
  It demonstrates how a raw LLM behaves before adding enterprise capabilities in later stages.
</p>

<hr>

<h2>Repository Structure</h2>

<pre><code>foundation_agent.py
requirements.txt
Procfile
.python-version
README.md
</code></pre>

<hr>

<h2>Run Locally</h2>

<ol>
  <li>
    Install dependencies:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>
    Set your API key:
    <pre><code>export GROQ_API_KEY="your_key_here"</code></pre>
  </li>
  <li>
    Run the app:
    <pre><code>streamlit run foundation_agent.py</code></pre>
  </li>
</ol>

<hr>

<h2>Deploying the App</h2>

<p>
  You can deploy this same repository to either <strong>Streamlit Cloud</strong> or <strong>Heroku</strong>.
</p>

<hr>

<h2>Deploy to Streamlit Cloud (recommended for simplicity)</h2>

<p>
  Streamlit Cloud automatically detects Streamlit apps and requires no Procfile.
</p>

<h3>Prerequisites</h3>

<ul>
  <li>
    Obtain a free Groq API key:
    <a href="https://console.groq.com/keys">https://console.groq.com/keys</a>
  </li>
  <li>Push this repo to your GitHub account.</li>
</ul>

<h3>Steps</h3>

<ol>
  <li>Go to <a href="https://share.streamlit.io">https://share.streamlit.io</a></li>
  <li>Connect your GitHub repository.</li>
  <li>Select <code>foundation_agent.py</code> as the entry point.</li>
  <li>
    Add an environment variable:
    <table>
      <thead>
        <tr>
          <th align="left">Name</th>
          <th align="left">Value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>GROQ_API_KEY</code></td>
          <td><code>your_key</code></td>
        </tr>
      </tbody>
    </table>
  </li>
  <li>Deploy.</li>
</ol>

<p>
  No <code>setup.sh</code> or runtime configuration is required.
</p>

<hr>

<h2>Deploy to Heroku</h2>

<p>
  Heroku uses the included <code>Procfile</code> and <code>.python-version</code>.
</p>

<h3>Prerequisites</h3>

<ul>
  <li>
    Obtain a free Groq API key:
    <a href="https://console.groq.com/keys">https://console.groq.com/keys</a>
  </li>
  <li>
    Fork the repo:
    <a href="https://github.com/lightningexperience/mas_workshop_foundation_agent">https://github.com/lightningexperience/mas_workshop_foundation_agent</a>
  </li>
</ul>

<h3>Option 1: Heroku CLI Deployment (Advanced)</h3>

<p>
  This option requires you to install the Heroku CLI.
</p>

<ol>
  <li>
    Login:
    <pre><code>heroku login</code></pre>
  </li>
  <li>
    Create an app:
    <pre><code>heroku create my-foundation-agent</code></pre>
  </li>
  <li>
    Set environment variable:
    <pre><code>heroku config:set GROQ_API_KEY="your_key_here"</code></pre>
  </li>
  <li>
    Deploy:
    <pre><code>git push heroku main</code></pre>
  </li>
  <li>
    Open the app:
    <pre><code>heroku open</code></pre>
  </li>
</ol>

<h3>Option 2: GitHub-Based Deployment (No CLI Required)</h3>

<p>
  This option uses the Heroku web interface and GitHub integration.
</p>

<ol>
  <li>Create App: Log into Heroku and create a new app via the dashboard.</li>
  <li>
    Add Monitoring (Optional): Go to the app’s <strong>Resources</strong> tab and add the
    <strong>Papertrail</strong> add-on (free edition).
  </li>
  <li>
    Connect GitHub:
    <ul>
      <li>Go to the <strong>Deploy</strong> tab.</li>
      <li>Select <strong>GitHub</strong> as the deployment method.</li>
      <li>Connect your GitHub account and select your forked repository.</li>
      <li>Under <strong>Automatic deploys</strong>, click <strong>Enable Automatic Deploys</strong>.</li>
    </ul>
  </li>
  <li>
    Set API Key:
    <ul>
      <li>Go to the <strong>Settings</strong> tab and click <strong>Reveal Config Vars</strong>.</li>
      <li>Set <code>GROQ_API_KEY</code> to your Groq API key value.</li>
    </ul>
  </li>
  <li>
    Initial Deploy: Return to the <strong>Deploy</strong> tab and click <strong>Deploy Branch</strong>.
  </li>
</ol>

<h3>One-Click Heroku Deployment</h3>

<p>
  <a href="https://heroku.com/deploy">
    <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
  </a>
</p>

<hr>

<h1> Files Needed for Deployment on Heroku</h1>
All files are already  included in the GitHub repo.
<h2>Procfile (already included)</h2>

<pre><code>web: streamlit run foundation_agent.py --server.port=$PORT --server.address=0.0.0.0</code></pre>

<hr>

<h2>.python-version (already included)</h2>

<pre><code>3.11</code></pre>

<p>
  Heroku will automatically select the latest patch version for Python 3.11 (for example, 3.11.14).
</p>

<hr>

<h2>requirements.txt (already included)</h2>

<pre><code>streamlit
groq
python-dotenv
</code></pre>

<hr>

<h2>Purpose of Stage 0</h2>

<p>
  This agent represents the “raw LLM” stage:
</p>

<ul>
  <li>No conversational memory</li>
  <li>No grounding or retrieval</li>
  <li>No actions</li>
  <li>No enterprise frameworks</li>
  <li>No LangChain</li>
</ul>

<p>
  This stage helps users understand the limitations of a simple LLM before introducing more advanced stages:
  Stage 1 (Enterprise Framework), Stage 2 (Grounding), Stage 3 (Action Agents), and Stage 4 (Orchestration).
</p>
