title: INFJ
menu: true


```mermaid
graph TD
%%classDef default width:25%;


Muse(("Serendipity<br>[[EN-5]]"))

Leader(("Dreamscaper<br>[[IN-1]]"))

Fool(("Self-Critic<br>[[IF-6]]"))

Priest(("Idealist<br>[[NF-f]]"))

Attitude(("Maker<br>[[IJ-f]]"))

CoreInt(("Visionary<br>[[NJ-f]]"))

SuppInt(("Messenger<br>[[FJ-f]]"))

Grip(("ES as Grip<br>[[ES-4-s]]"))

Vuln(("The Dictator<br>[[ET-7]]"))

Crisis(("Defeatist<br>[[ST-s]]"))

Desperation(("EP as Desperation<br>[[EP-s]]"))

Stuck(("SP as Stuck<br>[[SP-s]]"))

Trap(("The Critic<br>[[TP-s]]"))

Rival(("ES as Rival<br>[[ES-4-m]]"))

Adviser(("Empath<br>[[EF-2]]"))

Villain(("IS as Villain<br>[[IS-8]]"))

EgoCheck(("Delegator<br>[[EJ-m]]"))

Zoom(("SJ as Zoom<br>[[SJ-m]]"))

Understand(("SF as Understand<br>[[SF-m]]"))

Apprentice(("Reasoner<br>[[IT-3]]"))

Stretch(("NP as Stretch<br>[[NP-g]]"))

Discipline(("IP as Discipline<br>[[IP-g]]"))

Mindset(("NT as Mindset<br>[[NT-g]]"))

Discomfort(("TP as Discomfort<br>[[TP-g]]"))


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