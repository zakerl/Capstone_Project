## Merge workflow 

### Once main's protections are updated to 2 reviwers

#### 1. New task is assigned to you 
- Make a new branch. 
- Make relevant changes. 
- When happy push changes and do a pull request.

#### 2. Pull request on github.com
- Add whole team as relevant reviewers (2 people will end up doing the review, but in case someone can't, add all of us).
- See if your code passed relevant tests. (TBD)
- Push updates if tests aren't passed. 
- Inform your "go to" reviewers via Discord that your code needs to be reviewed.

#### 3. For Reviewers
- Look through tabs on github.com. "Commits", "Checks", "Files Changed".
- Once you've looked through file select "review changes" and leave feedback or approve.
- Reviewers, inform coder on Discord if they are good, or require further changes.

#### 4. Review Successful
- User who was waiting on review can now merge their changes with main.
- After merging. do >>>git checkout main | git pull. Confirm your changes work on main.

#### 5. Repeat as needed