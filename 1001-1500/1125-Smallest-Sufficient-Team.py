class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        skillsIndex = {skill: i for i, skill in enumerate(req_skills)}
        peopleSkills = []

        for person in people:
            skills = 0
            for skill in person:
                if skill in skillsIndex:
                    skills |= (1 << skillsIndex[skill])
            peopleSkills.append(skills)

        minTeam = {0: []}

        for i, personSkills in enumerate(peopleSkills):
            for currSkills in list(minTeam.keys()):
                newSkills = currSkills | personSkills
                if newSkills == currSkills:
                    continue
                if newSkills not in minTeam or len(minTeam[newSkills]) > len(minTeam[currSkills]) + 1:
                    minTeam[newSkills] = minTeam[currSkills] + [i]

        return minTeam[(1 << len(req_skills)) - 1] 
