title: ISFP
menu: true


```mermaid
graph TD
%%classDef default width:25%;


Muse(("EF as Muse<br>[[EF-5]]"))

Leader(("IF as Leader<br>[[IF-1]]"))

Fool(("IS as Fool<br>[[IS-6]]"))

Priest(("SF as Priest<br>[[SF-f]]"))

Attitude(("IP as Attitude<br>[[IP-f]]"))

CoreInt(("SP as CoreInt<br>[[SP-f]]"))

SuppInt(("FP as SuppInt<br>[[FP-f]]"))

Grip(("ET as Grip<br>[[ET-4-s]]"))

Vuln(("EN as Vuln<br>[[EN-7]]"))

Crisis(("NT as Crisis<br>[[NT-s]]"))

Desperation(("EJ as Desperation<br>[[EJ-s]]"))

Stuck(("NJ as Stuck<br>[[NJ-s]]"))

Trap(("TJ as Trap<br>[[TJ-s]]"))

Rival(("ET as Rival<br>[[ET-4-m]]"))

Adviser(("ES as Adviser<br>[[ES-2]]"))

Villain(("IT as Villain<br>[[IT-8]]"))

EgoCheck(("EP as EgoCheck<br>[[EP-m]]"))

Zoom(("NP as Zoom<br>[[NP-m]]"))

Understand(("NF as Understand<br>[[NF-m]]"))

Apprentice(("IN as Apprentice<br>[[IN-3]]"))

Stretch(("SJ as Stretch<br>[[SJ-g]]"))

Discipline(("IJ as Discipline<br>[[IJ-g]]"))

Mindset(("ST as Mindset<br>[[ST-g]]"))

Discomfort(("TJ as Discomfort<br>[[TJ-g]]"))


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