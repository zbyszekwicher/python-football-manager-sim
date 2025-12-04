\# ⚽ Python CLI Sim: Football Manager (System Modeling)



A large-scale, text-based simulation of managing the full lifecycle of a professional football (soccer) club. The project containing 25 files (modules) models complex economic, athletic, and personnel management systems. Developed in Python as a hobby project from 2020 to 2022.



\## 📅 Project Context \& Development Journey



\* \*\*Timeline:\*\* Developed during 2020–2022 as an ambitious self-taught project.

\* \*\*Key Learning:\*\* The initial \*\*procedural architecture\*\* (split across 25 files) resulted in complex cross-file dependencies and difficult debugging, highlighting the limitations of procedural programming for large applications — a crucial lesson that informed subsequent work using OOP (Object-Oriented Programming).



\## 🌟 Core Simulation Systems



This project models complex systems through algorithmic and data-driven methods:



\* \*\*Algorithmic Match Engine:\*\* Determines match outcomes, player statistics (goals/assists), and stamina loss using tiered probability lists based on calculated Offensive/Defensive strength ratings.

\* \*\*Financial \& Club Management:\*\* Tracks weekly budget, facility maintenance (stadium, training ground, youth academy), sponsorship contracts, and handles player transfers and fees.

\* \*\*Player Lifecycle:\*\* Players are generated with detailed attributes (skill, age, nationality, etc.) and progress through leveling and career retirement logic (`SeasonEnd.py`).

\* \*\*Persistence:\*\* The entire game state (team, roster, league, budget) is saved and loaded using Python's native file I/O functions.

\* \*\*Gameplay Loop:\*\* The game consist of seasons, each featuring a transfer window allowing for team upgrades as well as all the matches. Player need to manage the club's financial situation, squad strength, players' stamina (to avoid injuries), and club facilities like the youth academy, training grounds, and stadium. After all matches, player get the chance to be promoted to higher leagues. The goal is to build the strongest team possible and advance to the Premier League. While being hard (I never got to the Premier League myself), the game makes the constant progress sensible from season to season. As well a high level of team customization with an infinite number of procedurally generated players available and many tactics settings (team formations).



\## ⚠️ Known Issues (Legacy Code \& Dependencies)



This is a functional legacy project presented "as is" to showcase system design, not code elegance.



\* \*\*Structural Integrity:\*\* The core game loop relies on the \*\*exec(open().read())\*\* function for navigating between modules, which is an anti-pattern. This is the primary reason the project became difficult to debug.



\*\*However, I did not encounter any crashes or bugs, and the game is fully functional.\*\*

Yet, I cannot guarantee that it will never crash; fortunately the saves are very frequent.

Language Note: As a non-native English speaker, the primary focus during development was on logic and system functionality. Minor spelling or grammatical errors may be present in the game's text.



\## 🛠️ Setup and Running the Game



1\.  \*\*Clone the Repository:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/zbyszekwicher/python-football-manager-sim.git](https://github.com/zbyszekwicher/python-football-manager-sim.git)

&nbsp;   cd python-football-manager-sim

&nbsp;   ```



2.  \*\*Run the Main File:\*\*

&nbsp;   ```bash

&nbsp;   python \_FFManager\_app.py

&nbsp;   ```



Note: The game comes with a sample save file. It is called London Hienas by user1, and you can load it on game startup. Or you can start from scratch by typing any new nickname and new club name when prompted to create a fresh profile and begin in the National League (right before the transfer window).



