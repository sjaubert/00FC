# AGENTS

<skills_system priority="1">

## Available Skills

<!-- SKILLS_TABLE_START -->
<usage>
When users ask you to perform tasks, check if any of the available skills below can help complete the task more effectively. Skills provide specialized capabilities and domain knowledge.

How to use skills:
- Invoke: `npx openskills read <skill-name>` (run in your shell)
  - For multiple: `npx openskills read skill-one,skill-two`
- The skill content will load with detailed instructions on how to complete the task
- Base directory provided in output for resolving bundled resources (references/, scripts/, assets/)

Usage notes:
- Only use skills listed in <available_skills> below
- Do not invoke a skill that is already loaded in your context
- Each skill invocation is stateless
</usage>

<available_skills>

<skill>
<name>actualize</name>
<description>"Reconcile the project's FPF state with recent repository changes"</description>
<location>project</location>
</skill>

<skill>
<name>add-task</name>
<description>creates draft task file in .specs/tasks/draft/ with original user intent</description>
<location>project</location>
</skill>

<skill>
<name>add-typescript-best-practices</name>
<description>Setup TypeScript best practices and code style rules in CLAUDE.md</description>
<location>project</location>
</skill>

<skill>
<name>agent-evaluation</name>
<description>Evaluate and improve Claude Code commands, skills, and agents. Use when testing prompt effectiveness, validating context engineering choices, or measuring improvement quality.</description>
<location>project</location>
</skill>

<skill>
<name>analyse</name>
<description>Auto-selects best Kaizen method (Gemba Walk, Value Stream, or Muda) for target</description>
<location>project</location>
</skill>

<skill>
<name>analyse-problem</name>
<description>Comprehensive A3 one-page problem analysis with root cause and action plan</description>
<location>project</location>
</skill>

<skill>
<name>analyze-issue</name>
<description>Analyze a GitHub issue and create a detailed technical specification</description>
<location>project</location>
</skill>

<skill>
<name>apply-anthropic-skill-best-practices</name>
<description>Comprehensive guide for skill development based on Anthropic's official best practices - use for complex skills requiring detailed structure</description>
<location>project</location>
</skill>

<skill>
<name>attach-review-to-pr</name>
<description>Add line-specific review comments to pull requests using GitHub CLI API</description>
<location>project</location>
</skill>

<skill>
<name>brainstorm</name>
<description>Use when creating or developing, before writing code or implementation plans - refines rough ideas into fully-formed designs through collaborative questioning, alternative exploration, and incremental validation. Don't use during clear 'mechanical' processes</description>
<location>project</location>
</skill>

<skill>
<name>build-mcp</name>
<description>Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).</description>
<location>project</location>
</skill>

<skill>
<name>cause-and-effect</name>
<description>Systematic Fishbone analysis exploring problem causes across six categories</description>
<location>project</location>
</skill>

<skill>
<name>commit</name>
<description>Create well-formatted commits with conventional commit messages and emoji</description>
<location>project</location>
</skill>

<skill>
<name>compare-worktrees</name>
<description>Compare files and directories between git worktrees or worktree and current branch</description>
<location>project</location>
</skill>

<skill>
<name>context-engineering</name>
<description>Understand the components, mechanics, and constraints of context in agent systems. Use when writing, editing, or optimizing commands, skills, or sub-agents prompts.</description>
<location>project</location>
</skill>

<skill>
<name>create-agent</name>
<description>Comprehensive guide for creating Claude Code agents with proper structure, triggering conditions, system prompts, and validation - combines official Anthropic best practices with proven patterns</description>
<location>project</location>
</skill>

<skill>
<name>create-command</name>
<description>Interactive assistant for creating new Claude commands with proper structure, patterns, and MCP tool integration</description>
<location>project</location>
</skill>

<skill>
<name>create-hook</name>
<description>Create and configure git hooks with intelligent project analysis, suggestions, and automated testing</description>
<location>project</location>
</skill>

<skill>
<name>create-ideas</name>
<description>Generate ideas in one shot using creative sampling</description>
<location>project</location>
</skill>

<skill>
<name>create-pr</name>
<description>Create pull requests using GitHub CLI with proper templates and formatting</description>
<location>project</location>
</skill>

<skill>
<name>create-skill</name>
<description>Guide for creating effective skills. This command should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. Use when creating new skills, editing existing skills, or verifying skills work before deployment - applies TDD to process documentation by testing with subagents before writing, iterating until bulletproof against rationalization</description>
<location>project</location>
</skill>

<skill>
<name>create-workflow-command</name>
<description>Create a workflow command that orchestrates multi-step execution through sub-agents with file-based task prompts</description>
<location>project</location>
</skill>

<skill>
<name>create-worktree</name>
<description>Create and setup git worktrees for parallel development with automatic dependency installation</description>
<location>project</location>
</skill>

<skill>
<name>critique</name>
<description>Comprehensive multi-perspective review using specialized judges with debate and consensus building</description>
<location>project</location>
</skill>

<skill>
<name>decay</name>
<description>"Manage evidence freshness by identifying stale decisions and providing governance actions"</description>
<location>project</location>
</skill>

<skill>
<name>do-and-judge</name>
<description>Execute a task with sub-agent implementation and LLM-as-a-judge verification with automatic retry loop</description>
<location>project</location>
</skill>

<skill>
<name>do-competitively</name>
<description>Execute tasks through competitive multi-agent generation, multi-judge evaluation, and evidence-based synthesis</description>
<location>project</location>
</skill>

<skill>
<name>do-in-parallel</name>
<description>Launch multiple sub-agents in parallel to execute tasks across files or targets with intelligent model selection and quality-focused prompting</description>
<location>project</location>
</skill>

<skill>
<name>do-in-steps</name>
<description>Execute complex tasks through sequential sub-agent orchestration with intelligent model selection, and LLM-as-a-judge verification</description>
<location>project</location>
</skill>

<skill>
<name>fix-tests</name>
<description>Systematically fix all failing tests after business logic changes or refactoring</description>
<location>project</location>
</skill>

<skill>
<name>implement</name>
<description>Implement a task with automated LLM-as-Judge verification for critical steps</description>
<location>project</location>
</skill>

<skill>
<name>judge</name>
<description>Launch a sub-agent judge to evaluate results produced in the current conversation</description>
<location>project</location>
</skill>

<skill>
<name>judge-with-debate</name>
<description>Evaluate solutions through multi-round debate between independent judges until consensus</description>
<location>project</location>
</skill>

<skill>
<name>kaizen</name>
<description>Use when Code implementation and refactoring, architecturing or designing systems, process and workflow improvements, error handling and validation. Provide tehniquest to avoid over-engineering and apply iterative improvements.</description>
<location>project</location>
</skill>

<skill>
<name>launch-sub-agent</name>
<description>Launch an intelligent sub-agent with automatic model selection based on task complexity, specialized agent matching, Zero-shot CoT reasoning, and mandatory self-critique verification</description>
<location>project</location>
</skill>

<skill>
<name>load-issues</name>
<description>Load all open issues from GitHub and save them as markdown files</description>
<location>project</location>
</skill>

<skill>
<name>memorize</name>
<description>Curates insights from reflections and critiques into CLAUDE.md using Agentic Context Engineering</description>
<location>project</location>
</skill>

<skill>
<name>merge-worktree</name>
<description>Merge changes from worktrees into current branch with selective file checkout, cherry-picking, interactive patch selection, or manual merge</description>
<location>project</location>
</skill>

<skill>
<name>multi-agent-patterns</name>
<description>Design multi-agent architectures for complex tasks. Use when single-agent context limits are exceeded, when tasks decompose naturally into subtasks, or when specializing agents improves quality.</description>
<location>project</location>
</skill>

<skill>
<name>notes</name>
<description>Use when adding metadata to commits without changing history, tracking review status, test results, code quality annotations, or supplementing commit messages post-hoc - provides git notes commands and patterns for attaching non-invasive metadata to Git objects.</description>
<location>project</location>
</skill>

<skill>
<name>plan</name>
<description>Refine, parallelize, and verify a draft task specification into a fully planned implementation-ready task</description>
<location>project</location>
</skill>

<skill>
<name>plan-do-check-act</name>
<description>Iterative PDCA cycle for systematic experimentation and continuous improvement</description>
<location>project</location>
</skill>

<skill>
<name>prompt-engineering</name>
<description>Use this skill when you writing commands, hooks, skills for Agent, or prompts for sub agents or any other LLM interaction, including optimizing prompts, improving LLM outputs, or designing production prompt templates.</description>
<location>project</location>
</skill>

<skill>
<name>propose-hypotheses</name>
<description>Execute complete FPF cycle from hypothesis generation to decision</description>
<location>project</location>
</skill>

<skill>
<name>query</name>
<description>"Search the FPF knowledge base and display hypothesis details with assurance information"</description>
<location>project</location>
</skill>

<skill>
<name>reflect</name>
<description>Reflect on previus response and output, based on Self-refinement framework for iterative improvement with complexity triage and verification</description>
<location>project</location>
</skill>

<skill>
<name>reset</name>
<description>"Reset the FPF reasoning cycle to start fresh"</description>
<location>project</location>
</skill>

<skill>
<name>review-local-changes</name>
<description>Comprehensive review of local uncommitted changes using specialized agents with code improvement suggestions</description>
<location>project</location>
</skill>

<skill>
<name>review-pr</name>
<description>Comprehensive pull request review using specialized agents</description>
<location>project</location>
</skill>

<skill>
<name>root-cause-tracing</name>
<description>Use when errors occur deep in execution and you need to trace back to find the original trigger - systematically traces bugs backward through call stack, adding instrumentation when needed, to identify source of invalid data or incorrect behavior</description>
<location>project</location>
</skill>

<skill>
<name>setup-arxiv-mcp</name>
<description>Guide for setup arXiv paper search MCP server using Docker MCP</description>
<location>project</location>
</skill>

<skill>
<name>setup-code-formating</name>
<description>Sets up code formatting rules and style guidelines in CLAUDE.md</description>
<location>project</location>
</skill>

<skill>
<name>setup-codemap-cli</name>
<description>Guide for setup Codemap CLI for intelligent codebase visualization and navigation</description>
<location>project</location>
</skill>

<skill>
<name>setup-context7-mcp</name>
<description>Guide for setup Context7 MCP server to load documentation for specific technologies.</description>
<location>project</location>
</skill>

<skill>
<name>setup-serena-mcp</name>
<description>Guide for setup Serena MCP server for semantic code retrieval and editing capabilities</description>
<location>project</location>
</skill>

<skill>
<name>software-architecture</name>
<description>Guide for quality focused software architecture. This skill should be used when users want to write code, design architecture, analyze code, in any case that relates to software development.</description>
<location>project</location>
</skill>

<skill>
<name>status</name>
<description>"Display the current state of the FPF knowledge base"</description>
<location>project</location>
</skill>

<skill>
<name>subagent-driven-development</name>
<description>Use when executing implementation plans with independent tasks in the current session or facing 3+ independent issues that can be investigated without shared state or dependencies - dispatches fresh subagent for each task with code review between tasks, enabling fast iteration with quality gates</description>
<location>project</location>
</skill>

<skill>
<name>test-driven-development</name>
<description>Use when implementing any feature or bugfix, before writing implementation code - write the test first, watch it fail, write minimal code to pass; ensures tests actually verify behavior by requiring failure first</description>
<location>project</location>
</skill>

<skill>
<name>test-prompt</name>
<description>Use when creating or editing any prompt (commands, hooks, skills, subagent instructions) to verify it produces desired behavior - applies RED-GREEN-REFACTOR cycle to prompt engineering using subagents for isolated testing</description>
<location>project</location>
</skill>

<skill>
<name>test-skill</name>
<description>Use when creating or editing skills, before deployment, to verify they work under pressure and resist rationalization - applies RED-GREEN-REFACTOR cycle to process documentation by running baseline without skill, writing to address failures, iterating to close loopholes</description>
<location>project</location>
</skill>

<skill>
<name>thought-based-reasoning</name>
<description>Use when tackling complex reasoning tasks requiring step-by-step logic, multi-step arithmetic, commonsense reasoning, symbolic manipulation, or problems where simple prompting fails - provides comprehensive guide to Chain-of-Thought and related prompting techniques (Zero-shot CoT, Self-Consistency, Tree of Thoughts, Least-to-Most, ReAct, PAL, Reflexion) with templates, decision matrices, and research-backed patterns</description>
<location>project</location>
</skill>

<skill>
<name>tree-of-thoughts</name>
<description>Execute tasks through systematic exploration, pruning, and expansion using Tree of Thoughts methodology with multi-agent evaluation</description>
<location>project</location>
</skill>

<skill>
<name>update-docs</name>
<description>Update and maintain project documentation for local code changes using multi-agent workflow with tech-writer agents. Covers docs/, READMEs, JSDoc, and API documentation.</description>
<location>project</location>
</skill>

<skill>
<name>why</name>
<description>Iterative Five Whys root cause analysis drilling from symptoms to fundamentals</description>
<location>project</location>
</skill>

<skill>
<name>worktrees</name>
<description>Use when working on multiple branches simultaneously, context switching without stashing, reviewing PRs while developing, testing in isolation, or comparing implementations across branches - provides git worktree commands and workflow patterns for parallel development with multiple working directories.</description>
<location>project</location>
</skill>

<skill>
<name>write-concisely</name>
<description>Apply writing rules to any documentation that humans will read. Makes your writing clearer, stronger, and more professional.</description>
<location>project</location>
</skill>

<skill>
<name>write-tests</name>
<description>Systematically add test coverage for all local code changes using specialized review and development agents. Add tests for uncommitted changes (including untracked files), or if everything is commited, then will cover latest commit.</description>
<location>project</location>
</skill>

</available_skills>
<!-- SKILLS_TABLE_END -->

</skills_system>
