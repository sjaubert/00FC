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
<name>brainstorm</name>
<description>Use when creating or developing pedagogical content - refines rough ideas into fully-formed designs through collaborative questioning and incremental validation.</description>
<location>project</location>
</skill>

<skill>
<name>critique</name>
<description>Comprehensive multi-perspective review of a created document or pedagogical resource.</description>
<location>project</location>
</skill>

<skill>
<name>do-in-steps</name>
<description>Execute complex multi-file tasks through sequential orchestration. Use for creating full training modules with multiple documents.</description>
<location>project</location>
</skill>

<skill>
<name>write-concisely</name>
<description>Apply writing rules to documentation and pedagogical supports. Makes content clearer, stronger, and more professional.</description>
<location>project</location>
</skill>

<skill>
<name>commit</name>
<description>Create well-formatted git commits with conventional commit messages.</description>
<location>project</location>
</skill>

<skill>
<name>reflect</name>
<description>Reflect on a previous response and iteratively improve it based on self-refinement framework.</description>
<location>project</location>
</skill>

<skill>
<name>analyse-problem</name>
<description>Comprehensive A3 one-page problem analysis with root cause and action plan. Useful for quality/industrial engineering contexts.</description>
<location>project</location>
</skill>

<skill>
<name>cause-and-effect</name>
<description>Systematic Fishbone (Ishikawa) analysis exploring problem causes across six categories. Relevant for BTS ATI industrial content.</description>
<location>project</location>
</skill>

<skill>
<name>plan-do-check-act</name>
<description>Iterative PDCA cycle for systematic experimentation and continuous improvement. Core BTS ATI methodology.</description>
<location>project</location>
</skill>

<skill>
<name>why</name>
<description>Iterative Five Whys root cause analysis. Core tool for BTS ATI quality modules.</description>
<location>project</location>
</skill>

</available_skills>
<!-- SKILLS_TABLE_END -->

</skills_system>
