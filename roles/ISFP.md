title: ISFP
menu: true


```mermaid
graph TD
%%classDef default width:25%;


Muse(("[[EF-5|EF as Muse]]"))

Leader(("[[IF-1|IF as Leader]]"))

Fool(("[[IS-6|IS as Fool]]"))

Priest(("[[SF-f|SF as Priest]]"))

Attitude(("[[IP-f|IP as Attitude]]"))

CoreInt(("[[SP-f|SP as CoreInt]]"))

SuppInt(("[[FP-f|FP as SuppInt]]"))

Grip(("[[ET-4-s|ET as Grip]]"))

Vuln(("[[EN-7|EN as Vuln]]"))

Crisis(("[[NT-s|NT as Crisis]]"))

Desperation(("[[EJ-s|EJ as Desperation]]"))

Stuck(("[[NJ-s|NJ as Stuck]]"))

Trap(("[[TJ-s|TJ as Trap]]"))

Rival(("[[ET-4-m|ET as Rival]]"))

Adviser(("[[ES-2|ES as Adviser]]"))

Villain(("[[IT-8|IT as Villain]]"))

EgoCheck(("[[EP-m|EP as EgoCheck]]"))

Zoom(("[[NP-m|NP as Zoom]]"))

Understand(("[[NF-m|NF as Understand]]"))

Apprentice(("[[IN-3|IN as Apprentice]]"))

Stretch(("[[SJ-g|SJ as Stretch]]"))

Discipline(("[[IJ-g|IJ as Discipline]]"))

Mindset(("[[ST-g|ST as Mindset]]"))

Discomfort(("[[TJ-g|TJ as Discomfort]]"))


subgraph Government
    Leader -->|Values|Priest
    Leader -->|Identity|Attitude
    Leader -->|"Senior Aide"|CoreInt
    Leader --> |"Aide"|SuppInt
end


subgraph Stress
    Vuln
    Crisis
    Stuck
    Trap
    Attitude -->|Desperation|Desperation
    Leader ---> Grip 
end


subgraph Elders
    Adviser --> |Mentor|Leader
    EgoCheck --> |"Ego Check"|Attitude
    Zoom -->|Input|CoreInt
    Understand -->|Perspective|Priest
    Rival --> Leader
end

Adviser -->|Balanced by|Villain
%%Vuln --->|Criticism| Fool 

subgraph Growth
    Leader --> |Challenge|Apprentice
    Stretch
    Priest -->|Challenge|Mindset
    Discipline
    Discomfort
    Apprentice -->|Reaction|Vuln
end

Attitude -->|Discipline|Discipline
Discipline -->|Obsession|Desperation

CoreInt --> |Stretch|Stretch
SuppInt -->|Discomfort|Discomfort
Discomfort --> |Trap|Trap

Stretch --> |Wall|Stuck

Mindset -->|Identity Crisis|Crisis

%% Rival - Inf - 4
%%Rival -->|Challenge|Leader
%%Adviser -->|Mediate|Rival

%% Villain - Demon - 8
Villain --> |Temptation|Leader

%% Fool/Critic - 6
%%Fool -->|Feeds|Rival
Fool -->|Disrupts| Apprentice
%%Adviser --->|Challenged by|Fool
Fool -->|Challenges|Adviser

%% Muse - Opp - 5
Muse -->|Inspire|Apprentice

```