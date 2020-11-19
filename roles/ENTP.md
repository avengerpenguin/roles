title: ENTP
menu: true


```mermaid
graph TD
%%classDef default width:25%;


Muse(("Epiphany<br>[[IN-5]]"))

Leader(("Seeker<br>[[EN-1]]"))

Fool(("Disrupter<br>[[ET-6]]"))

Priest(("Innovator<br>[[NT-f]]"))

Attitude(("Disruptor<br>[[EP-f]]"))

CoreInt(("Creative<br>[[NP-f]]"))

SuppInt(("Analyst<br>[[TP-f]]"))

Grip(("IS as Grip<br>[[IS-4-s]]"))

Vuln(("Rebel<br>[[IF-7]]"))

Crisis(("The Attention-Seeker<br>[[SF-s]]"))

Desperation(("Zealot<br>[[IJ-s]]"))

Stuck(("SJ as Stuck<br>[[SJ-s]]"))

Trap(("Ranter<br>[[FJ-s]]"))

Rival(("IS as Rival<br>[[IS-4-m]]"))

Adviser(("Scientist<br>[[IT-2]]"))

Villain(("Hedonist<br>[[ES-8]]"))

EgoCheck(("Validator<br>[[IP-m]]"))

Zoom(("SP as Zoom<br>[[SP-m]]"))

Understand(("ST as Understand<br>[[ST-m]]"))

Apprentice(("Conversationalist<br>[[EF-3]]"))

Stretch(("NJ as Stretch<br>[[NJ-g]]"))

Discipline(("Prototyper<br>[[EJ-g]]"))

Mindset(("The Dreamer<br>[[NF-g]]"))

Discomfort(("Orator<br>[[FJ-g]]"))


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