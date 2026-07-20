<div align="center">
  <img src="./assets/hero.svg" width="100%" alt="Harshit Tyagi - Sunset Hero" />

  <br/><br/>

  <a href="https://github.com/Harshit07ank"><img src="https://img.shields.io/badge/GitHub-Harshit07ank-ff3366?style=for-the-badge&logo=github&logoColor=white&labelColor=0a050f" /></a>
  <img src="https://img.shields.io/badge/Status-Building_Shaders-ff5e36?style=for-the-badge&labelColor=0a050f" />

  <br/><br/>

  **[🧠 Mindset](#engineering-mindset) · [🛠️ Log](#engineering-log) · [💼 Work](#selected-work) · [🗺️ Journey](#engineering-journey) · [🧰 Toolbox](#toolbox) · [📊 Stats](#github-stats) · [🔭 Exploring](#things-im-exploring) · [🤝 Connect](#connect)**

</div>

---

## 🧠 Engineering Mindset
<a id="engineering-mindset"></a>

I learn best by building — usually by picking something a bit too hard and figuring out how it actually works, not just how to use it. Most of what I build lives in the JavaScript ecosystem: backend systems, AI integrations, software design, and interactive experiences.

### Mindset & Flow Architecture

Below is a system architecture map of how I approach structuring and orchestrating applications from backend to interactive frontend:

```mermaid
graph TD
    User([User]) -->|Interacts| UI[Three.js / React Frontend]
    UI -->|API Requests| Gateway[Gateway / Route Handlers]
    Gateway -->|Auth & Validation| Controller[Logic Controller]
    Controller -->|Query / RAG Pipeline| AI[Gemini API / VectorDB]
    Controller -->|Data Persistence| DB[(Database / Firestore)]
    Controller -->|Realtime Sim| Engine[Physics Particle Engine]
    
    style User fill:#050510,stroke:#ff3366,stroke-width:2px,color:#ffffff
    style UI fill:#12081a,stroke:#ff6633,stroke-width:2px,color:#ffffff
    style Gateway fill:#12081a,stroke:#ffcc33,stroke-width:2px,color:#ffffff
    style Controller fill:#12081a,stroke:#ff3366,stroke-width:2px,color:#ffffff
    style AI fill:#12081a,stroke:#ff6633,stroke-width:2px,color:#ffffff
    style DB fill:#12081a,stroke:#ffcc33,stroke-width:2px,color:#ffffff
    style Engine fill:#12081a,stroke:#ff3366,stroke-width:2px,color:#ffffff
```

<br/>

## 🛠️ Engineering Log
<a id="engineering-log"></a>

Right now: a real-time water simulation in Three.js — `InstancedMesh` particles with a custom `ShaderMaterial` for streak rendering. I picked it to force myself into shader math and performance work that typical backend projects don't demand.

Current problem: keeping turbulence and splash timing convincing without tanking frame time at thousands of particles.

<br/>

## 💼 Selected Work
<a id="selected-work"></a>

**🔗 [CHITEASE](https://github.com/Harshit07ank/CHITEASE)**
<br/>
<img src="./assets/chitease-preview.png.png" width="500" alt="CHITEASE preview" style="border-radius: 10px;" />
<br/>
AI-powered digital chit fund platform — secure workflows, automation, and AI-assisted verification for traditional chit funds.
<br/>
<img src="https://img.shields.io/badge/JavaScript-ff3366?style=flat-square&logo=javascript&logoColor=white" /> <img src="https://img.shields.io/badge/MERN_Stack-ff5e36?style=flat-square&logo=mongodb&logoColor=white" /> <img src="https://img.shields.io/badge/AI_Integration-ffcc33?style=flat-square&logo=openai&logoColor=white" />

<br/>

**🔗 [IRIS](https://github.com/Harshit07ank/IRIS)**
<br/>
<img src="./assets/iris-preview.png.png" width="500" alt="IRIS preview" style="border-radius: 10px;" />
<br/>
Vision through voice — an accessibility platform combining multimodal AI, speech recognition, and voice interaction.
<br/>
<img src="https://img.shields.io/badge/JavaScript-ff3366?style=flat-square&logo=javascript&logoColor=white" /> <img src="https://img.shields.io/badge/Gemini_API-ff5e36?style=flat-square&logo=google&logoColor=white" /> <img src="https://img.shields.io/badge/Accessibility-ffcc33?style=flat-square" />

<br/>

**🚧 Interactive Portfolio** — *in progress*
<br/>
<img src="./assets/world-preview.png" width="500" alt="Interactive Portfolio Preview" style="border-radius: 10px;" />
<br/>
Story-driven portfolio with procedural environments; the proving ground for the rendering work above.
<br/>
<img src="https://img.shields.io/badge/Three.js-ff3366?style=flat-square&logo=threedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/WebGL-ff5e36?style=flat-square&logo=webgl&logoColor=white" /> <img src="https://img.shields.io/badge/GLSL-ffcc33?style=flat-square&logo=opengl&logoColor=white" />

<br/>

**🚧 Procedural World Engine** — *early-stage*
<br/>
<img src="./assets/graphics-preview.png" width="500" alt="Procedural World Engine Preview" style="border-radius: 10px;" />
<br/>
Terrain generation, shaders, and rendering-optimization experiments.
<br/>
<img src="https://img.shields.io/badge/WebGL-ff3366?style=flat-square&logo=webgl&logoColor=white" /> <img src="https://img.shields.io/badge/GLSL-ff5e36?style=flat-square&logo=opengl&logoColor=white" /> <img src="https://img.shields.io/badge/Procedural_Generation-ffcc33?style=flat-square" />

<br/>

## 🗺️ Engineering Journey
<a id="engineering-journey"></a>

```mermaid
timeline
    title My Engineering Journey
    2023 : Learning by building : Deep dive into fundamentals
    2024 : Full Stack Systems : MERN & scalable web apps
    2025 : AI Integrations : RAG pipelines & Gemini API
    2026 : Graphics & WebGL : Shaders, particles, and Three.js
    Now : Architecture & Systems : Scaling backends and optimization
```

<details>
<summary><strong>🌅 View Visual Timeline</strong></summary>
<br/>
<p align="center">
  <img src="./assets/timeline.png" width="100%" alt="Visual Journey Timeline" style="border-radius: 10px;" />
</p>
</details>

<br/>

**What's next?**
<br/>
<p align="center">
  <img src="https://img.shields.io/badge/Software%20Architecture-ff3366?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Distributed%20Systems-ff5e36?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CI%2FCD%20Pipelines-ffcc33?style=for-the-badge" />
  <img src="https://img.shields.io/badge/GPU%20Programming-ff3366?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend%20System%20Design-ff5e36?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI%20Workflows-ffcc33?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Performance%20Optimization-ff3366?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Creative%20Technology-ff5e36?style=for-the-badge" />
</p>

<br/>

## 🧰 Toolbox
<a id="toolbox"></a>

<div align="center">

  <img src="https://skillicons.dev/icons?i=js,react,nextjs,nodejs,express,mongodb,firebase,threejs,html,css,git,vscode&theme=dark" />

  <br/><br/>

  <details>
    <summary><strong>🎨 Creative Tech Stack</strong></summary>
    <br/>
    <p align="left">
      <img src="https://img.shields.io/badge/Three.js-ff3366?style=flat-square&logo=threedotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/WebGL-ff5e36?style=flat-square&logo=webgl&logoColor=white" />
      <img src="https://img.shields.io/badge/GLSL_Shaders-ffcc33?style=flat-square" />
      <img src="https://img.shields.io/badge/Canvas_API-ff3366?style=flat-square" />
      <img src="https://img.shields.io/badge/Framer_Motion-ff5e36?style=flat-square&logo=framer&logoColor=white" />
    </p>
  </details>

  <details>
    <summary><strong>🖥️ Front End Stack</strong></summary>
    <br/>
    <p align="left">
      <img src="https://img.shields.io/badge/React-ff3366?style=flat-square&logo=react&logoColor=white" />
      <img src="https://img.shields.io/badge/Next.js-ff5e36?style=flat-square&logo=nextdotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/Redux-ffcc33?style=flat-square&logo=redux&logoColor=white" />
      <img src="https://img.shields.io/badge/TailwindCSS-ff3366?style=flat-square&logo=tailwindcss&logoColor=white" />
      <img src="https://img.shields.io/badge/HTML5/CSS3-ff5e36?style=flat-square&logo=html5&logoColor=white" />
    </p>
  </details>

  <details>
    <summary><strong>⚙️ Backend &amp; Database</strong></summary>
    <br/>
    <p align="left">
      <img src="https://img.shields.io/badge/Node.js-ff3366?style=flat-square&logo=nodedotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/Express-ff5e36?style=flat-square&logo=express&logoColor=white" />
      <img src="https://img.shields.io/badge/MongoDB-ffcc33?style=flat-square&logo=mongodb&logoColor=white" />
      <img src="https://img.shields.io/badge/Firebase-ff3366?style=flat-square&logo=firebase&logoColor=white" />
      <img src="https://img.shields.io/badge/REST_APIs-ff5e36?style=flat-square" />
      <img src="https://img.shields.io/badge/GraphQL-ffcc33?style=flat-square&logo=graphql&logoColor=white" />
    </p>
  </details>

  <details>
    <summary><strong>☁️ Cloud &amp; DevOps</strong></summary>
    <br/>
    <p align="left">
      <img src="https://img.shields.io/badge/Vercel-ff3366?style=flat-square&logo=vercel&logoColor=white" />
      <img src="https://img.shields.io/badge/Docker-ff5e36?style=flat-square&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/GitHub_Actions-ffcc33?style=flat-square&logo=githubactions&logoColor=white" />
      <img src="https://img.shields.io/badge/Git-ff3366?style=flat-square&logo=git&logoColor=white" />
    </p>
  </details>

  <details>
    <summary><strong>🧠 Programming Languages</strong></summary>
    <br/>
    <p align="left">
      <img src="https://img.shields.io/badge/JavaScript-ff3366?style=flat-square&logo=javascript&logoColor=white" />
      <img src="https://img.shields.io/badge/TypeScript-ff5e36?style=flat-square&logo=typescript&logoColor=white" />
      <img src="https://img.shields.io/badge/HTML/CSS-ffcc33?style=flat-square" />
      <img src="https://img.shields.io/badge/C/C++-ff3366?style=flat-square&logo=c&logoColor=white" />
      <img src="https://img.shields.io/badge/Python-ff5e36?style=flat-square&logo=python&logoColor=white" />
    </p>
  </details>

</div>

<br/>

## 📊 GitHub Stats
<a id="github-stats"></a>

<div align="center">

  <img src="https://github-readme-stats.vercel.app/api?username=Harshit07ank&show_icons=true&theme=dark&bg_color=0a050f&border_color=ff3366&title_color=ff5e36&icon_color=ffcc33&hide_border=true" height="165" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Harshit07ank&layout=compact&theme=dark&bg_color=0a050f&border_color=ff3366&title_color=ff5e36&hide_border=true" height="165" />
  <br/>
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=Harshit07ank&theme=dark&background=0a050f&border=ff3366&ring=ff5e36&fire=ffcc33&hide_border=true" />

  <br/><br/>

  <img src="https://raw.githubusercontent.com/Harshit07ank/Harshit07ank/output/github-contribution-grid-snake-dark.svg" alt="Contribution Snake" />

</div>

<br/>

## 🔭 Things I'm Exploring
<a id="things-im-exploring"></a>

> Topics I keep coming back to, outside of what I'm actively shipping:

**Software Architecture** · **Distributed Systems** · **CI/CD Pipelines** · **AI Workflows** · **Backend Systems** · **Performance Optimization** · **Interactive Experiences** · **Cloud Deployment**

<br/>

## 🤝 Connect
<a id="connect"></a>

<div align="center">

  <a href="#" title="Let's connect on LinkedIn"><img src="https://img.shields.io/badge/LinkedIn-0a050f?style=for-the-badge&logo=linkedin&logoColor=ff5e36" /></a>
  <a href="#" title="Follow along on X / Twitter"><img src="https://img.shields.io/badge/Twitter-0a050f?style=for-the-badge&logo=x&logoColor=ffcc33" /></a>
  <a href="mailto:#" title="Send me an email"><img src="https://img.shields.io/badge/Email-0a050f?style=for-the-badge&logo=gmail&logoColor=ff3366" /></a>

</div>

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=ff3366,ff6633,ffcc33&height=120&section=footer" width="100%" />
