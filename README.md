# UFC Stats Scraper

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)


## Data Structure

Fighter stats

- fighter_id
- name
- height
- weight
- reach
- stance
- dob
- weightclass
- active
- fight_time_total
- fight_time_avg
- n_win
- n_loss
- n_draw
- Sig_Str_land_pM - Significant Strikes Landed per Minute
- Sig_Str_land_pct - Significant Striking Accuracy (% landed)
- Sig_Str_abs_pM - Significant Strikes Absorbed per Minute
- Sig_Str_def_pct - Significant Strike Defence (the % of opponents strikes that did not land)
- TD_Avg - Average Takedowns Landed per 15 minutes
- TD_land_pct - Takedown Accuracy
- TD_def_pct - Takedown Defense (the % of opponents TD attempts that did not land)
- Sub_Avg - Average Submissions Attempted per 15 minutes

Fighter performance

- fighter_id
- fight_id
- date
- outcome - Win/Loss/Draw
- KD - Knockdown landed
- Sig_Str_att - Significant strikes attempted
- Sig_Str_land - Significant strikes landed
- Sig_Str_land_pct - % Significant strikes landed
- Str_att - Strikes attempted
- Str_land - Strikes landed
- Str_land_pct - % Strikes landed
- TD_att - Takedowns attempted
- TD_land - Takedowns landed
- TD_land_pct - % Takedowns landed
- Sub_att - Submissions attempted
- Pass
- Rev
- Head_att - Significant strikes attempted to Head
- Head_land - Significant strikes landed to Head
- Body_att - Significant strikes attempted to Body
- Body_land - Significant strikes landed to Body
- Leg_att - Significant strikes attempted to Leg
- Leg_land - Significant strikes landed to Leg
- Distance_att - Significant strikes attempted from Distance
- Distance_land - Significant strikes landed from Distance
- Clinch_att - Significant strikes attempted from Clinch
- Clinch_land - Significant strikes landed from Clinch
- Ground_att - Significant strikes attempted from Ground
- Ground_land - Significant strikes landed from Ground
- Sig_Str_abs - Significant strikes absorbed (opponent's strikes landed)
- Sig_Str_def - Significant strikes defended (opponent's strikes did not land)
- Str_abs - Strikes absorbed
- Str_def - Strikes defended
- TD_abs - Takedowns absorbed
- TD_def - Takedowns defended
- Head_abs
- Head_def
- Body_abs
- Body_def
- Leg_abs
- Leg_def
- Distance_abs
- Distance_def
- Clinch_abs
- Clinch_def
- Ground_abs
- Ground_def

Fights

- fight_id
- date
- location
- fighter_1
- fighter_1_id
- fighter_2
- fighter_2_id
- winner
- weight_class
- title_bout
- decision_method
- time_format
- fight_duration_lastrnd
- fight_duration_lastrnd_time



## About <a name = "about"></a>

Write about 1-2 paragraphs describing the purpose of your project.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Usage <a name = "usage"></a>

Add notes about how to use the system.
