# Vault Connection Options Map

[한국어](solution-map.md)

## Checklist of 8 Candidates

The official documentation and Muse web screens were checked on **2026-11-05**. Muse has a free tier with limited usage, and storage plans or a Claude subscription apply separately. [Meta Muse usage guide](https://ai.meta.com/muse/)

| Candidate | Source and screen observation | Cost · install · limits to check |
|---|---|---|
| A · Dropbox mirror copy | Checked in the Dropbox official help and the Muse Business list. [Dropbox help](https://help.dropbox.com/integrations/connect-to-meta-muse) | All Dropbox plans in the US · Canada. Needs account connection in a browser, and has settings per action such as read · write · delete · share. Whether it allows only a specific folder, and whether files come back to the home PC automatically, need testing. |
| B · GitHub private mirror copy | Checked in Meta's official announcement and the Muse Business list. [Meta Connect announcement](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) | Needs a GitHub account and a test repository. Separate connector cost, and whether it can be limited to one private repository, are unverified. |
| C · Google Drive or Box | Both items checked on the Muse screen. Meta officially announced Box and gives a policy on data from Google connections. [Meta Connect announcement](https://www.meta.com/blog/meta-connect-2026-everything-we-announced/) · [Meta connector help](https://www.meta.com/help/superintelligence/1687253048996149/) | Needs an account for each service. Separate cost of the connection is unverified. Drive shows settings per action for read · write · delete · share and background actions. The single-folder access scope cannot be judged from the action settings on the screen alone. Box's actual permission scope is unverified. |
| D · Manual transfer | Library download and Codex handoff confirmed by hands-on proof with the vault. [M3 Lab 4](../../vl_worklog/20261105_M3_Muse-My-Workflow.md#실습-4-결과) | Possible in a browser without connecting separate storage. Downloading and copying to the Inbox are manual; preservation of the 3 original files was verified. |
| E · Claude Code Remote Control | Checked Anthropic's official documentation and hands-on proof from an earlier Topic. [Anthropic Remote Control](https://code.claude.com/docs/en/remote-control) · [Earlier Topic conclusion](../../../Claude-Code-Mobile-Remote-Execution/README.md#이-자료의-결론) | Needs a supported Claude subscription and local Claude Code. The home PC must be running and online, and the work folder is read locally. |
| F · Claude Code web · mobile | Cloud sessions and GitHub integration checked in Anthropic's official documentation. [Claude Code cloud](https://code.claude.com/docs/en/claude-code-on-the-web) · [Claude pricing](https://claude.com/pricing) | Needs a plan that supports Claude Code and GitHub access. The install scope of the Claude GitHub App differs from the scope of a local token connection. In this lab, a separate test repo is a prerequisite. |
| G · Muse desktop | macOS confirmed on Meta's download page. Microsoft announced upcoming Windows MXC integration. [Meta download](https://ai.meta.com/muse/download/) · [Microsoft Windows announcement](https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/) | Needs a Mac app install. A Windows install release and separate cost could not be confirmed in this check of official documentation, so the Windows test is on hold. |
| H · Custom connector | Meta gives guidance on custom connectors. [Meta connector help](https://www.meta.com/help/superintelligence/1687253048996149/) | May need an API · credentials and running a service. The access scope and running cost of connecting directly to the home PC are unverified. This time it is document review only. |

## Proposed Candidates to Test

| Order | Candidate | What to check |
|---|---|---|
| 1 | D · Manual download | Use as the baseline: the steps that must be done by hand in S1 · S2, and source preservation. |
| 2 | E · Remote Control | Compare the steps it takes to continue home work on the phone in S2 · S4, and the condition that the PC must be running. |
| 3 | C · Google Drive | Once the user sets the test scope, look at search and retrieval in S3 · S5 with public samples. Record file actions and folder scope separately. |
| 4 | A · Dropbox | If a new connection is decided, compare under the same conditions as Drive in a test space that holds only public samples. |

The candidates are at the proposal stage. Before any storage test, set the mirror copy rules and the read · write scope first. [M4 lab order](../../vl_roadmap/20261018_RoadMap_Muse-My-Workflow.md#m4---볼트-연결-해법--집과-밖을-끊김-없이)
