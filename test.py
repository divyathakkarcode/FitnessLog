from classDefinition import Person
from classDefinition import workoutSession
from classDefinition import Routine

# -------------------------- Testing for Person Class --------------------------
# ------------------------------------------------------------------------------
print("------------ Testing for Person Class ---------------")
testUser = Person("MrKanister12", 20, 140, [], [])
print(testUser.username)
print(testUser.age)
print(testUser.weight)
try:
	print(testUser.personalRoutines[0].routineName)
	print(testUser.personalRoutines[0].exercisesArray)
	print(testUser.personalRoutines[0].targetRepsArray)
	print(testUser.personalRoutines[0].targetSetsArray)
	print(testUser.personalRoutines[1].routineName)
	print(testUser.personalRoutines[1].exercisesArray)
	print(testUser.personalRoutines[1].targetRepsArray)
	print(testUser.personalRoutines[1].targetSetsArray)
	print(testUser.personalRoutines[2].routineName)
	print(testUser.personalRoutines[2].exercisesArray)
	print(testUser.personalRoutines[2].targetRepsArray)
	print(testUser.personalRoutines[2].targetSetsArray)
except IndexError:
	print("No routines have been added yet so you can't index the personalRoutines array")

# -------------------------- Testing for Routine Class --------------------------
# ------------------------------------------------------------------------------
print("------------ Testing for Routine Class ---------------")
pushRoutine = Routine("Push", ["Push Ups", "Bench Press", "Shoulder Press"], [25, 8, 5], [3, 3, 3])
print("---------------------------")
print(pushRoutine.routineName)
print(pushRoutine.exercisesArray)
print(pushRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)

pullRoutine = Routine("Pull", ["Pull Ups", "Deadlifts", "Bicep Curls"], [10, 8, 16], [4, 4, 4])
print("---------------------------")
print(pullRoutine.routineName)
print(pullRoutine.exercisesArray)
print(pullRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)

legsRoutine = Routine("Legs", ["Squats", "Lunges", "Glute Bridges"], [30, 10, 6], [5, 5, 5])
print("---------------------------")
print(legsRoutine.routineName)
print(legsRoutine.exercisesArray)
print(legsRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)

# -------------------------- Testing for addPersonalRoutine Class --------------------------
# ------------------------------------------------------------------------------
print("------------ Testing for addPersonalRoutine Class ---------------")
testUser.addPersonalRoutine(pushRoutine)
testUser.addPersonalRoutine(pullRoutine)
testUser.addPersonalRoutine(legsRoutine)
print("---------------------------")
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.personalRoutines[0].routineName)
print(testUser.personalRoutines[0].exercisesArray)
print(testUser.personalRoutines[0].targetRepsArray)
print(testUser.personalRoutines[0].targetSetsArray)
print(testUser.personalRoutines[1].routineName)
print(testUser.personalRoutines[1].exercisesArray)
print(testUser.personalRoutines[1].targetRepsArray)
print(testUser.personalRoutines[1].targetSetsArray)
print(testUser.personalRoutines[2].routineName)
print(testUser.personalRoutines[2].exercisesArray)
print(testUser.personalRoutines[2].targetRepsArray)
print(testUser.personalRoutines[2].targetSetsArray)

# -------------------------- Testing for rest of Person Class methods --------------------------
# ------------------------------------------------------------------------------
print("------------ Testing for rest of Person Class methods ---------------")
testUser.deletePersonalRoutine("Pull")
testUser.editUsername("NinjasHyper")
testUser.editAge(21)
testUser.editWeight(225)

print("---------------------------")
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.personalRoutines[0].routineName)
print(testUser.personalRoutines[0].exercisesArray)
print(testUser.personalRoutines[0].targetRepsArray)
print(testUser.personalRoutines[0].targetSetsArray)
print(testUser.personalRoutines[1].routineName)
print(testUser.personalRoutines[1].exercisesArray)
print(testUser.personalRoutines[1].targetRepsArray)
print(testUser.personalRoutines[1].targetSetsArray)
try:
	print(testUser.personalRoutines[2].routineName)
	print(testUser.personalRoutines[2].exercisesArray)
	print(testUser.personalRoutines[2].targetRepsArray)
	print(testUser.personalRoutines[2].targetSetsArray)
except IndexError:
	print("Pull routine was successfully deleted")

testUser.deletePersonalRoutine("Non-Existant Workout")



# -------------------------- Testing for Routine Class --------------------------
# ------------------------------------------------------------------------------
print("------------ Testing for Routine Class ---------------")

pushRoutine.addExercise("Tricep Dips", 10, 4)
print(pushRoutine.routineName)
print(pushRoutine.exercisesArray)
print(pushRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)
print("---------------------------")
pushRoutine.editRoutineName("Intermediate test Updated Push Routine Name")
pushRoutine.deleteExercise("Shoulder Press")
print(pushRoutine.routineName)
print(pushRoutine.exercisesArray)
print(pushRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)
pushRoutine.edittargetRepsArray([1,2,3])
pushRoutine.edittargetSetsArray([4,5,6])
print(pushRoutine.routineName)
print(pushRoutine.exercisesArray)
print(pushRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)
print("---------------------------")
pushRoutine.editRoutineName("Push")



# -------------------------- Testing for workoutSession Class --------------------------
# ------------------------------------------------------------------------------
print("------------ Testing for workoutSession Class ---------------")
Jan1Session = workoutSession(2021, 1, 1, pushRoutine, "I only completed half the reps for the last set of bench press")
Jan2Session = workoutSession(2021, 1, 2, pullRoutine, "I had to deadlift with a different bar")
Jan4Session = workoutSession(2021, 1, 4, legsRoutine, "Haven't done legs in 1 month, so felt sore")
Jan8Session = workoutSession(2021, 1, 8, pushRoutine, "Very good workout today")
print("------------------")
print(Jan1Session.date)
print(Jan1Session.routine.routineName)
print(Jan1Session.note)
print("------------------")
print(Jan2Session.date)
print(Jan2Session.routine.routineName)
print(Jan2Session.note)
print("------------------")
print(Jan4Session.date)
print(Jan4Session.routine.routineName)
print(Jan4Session.note)
print("------------------")
print(Jan8Session.date)
print(Jan8Session.routine.routineName)
print(Jan8Session.note)

print("------------ Testing for Sessions added to a User Profile---------------")
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.workoutHistoryArray)
testUser.addWorkoutSession(Jan2Session)
print(testUser.workoutHistoryArray)
testUser.addWorkoutSession(Jan4Session)
print(testUser.workoutHistoryArray)
testUser.addWorkoutSession(Jan8Session)
print(testUser.workoutHistoryArray)
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.workoutHistoryArray[0].date)
print(testUser.workoutHistoryArray[0].routine.routineName)
print(testUser.workoutHistoryArray[0].note)
print(testUser.workoutHistoryArray[1].date)
print(testUser.workoutHistoryArray[1].routine.routineName)
print(testUser.workoutHistoryArray[1].note)
print(testUser.workoutHistoryArray[2].date)
print(testUser.workoutHistoryArray[2].routine.routineName)
print(testUser.workoutHistoryArray[2].note)
print("------------ Testing for Sessions deleted from a User Profile---------------")
print("------------ Some Editing Verifications on User Profile Carrying Over Also Tested Here ---------------")
testUser.deleteWorkoutSession(2021, 1, 4)
pushRoutine.editRoutineName("John Cena Type Push Workout")
pushRoutine.addExercise("Pec Fly Machine", 1000, 1000)
print("---------------------------")
print(pushRoutine.routineName)
print(pushRoutine.exercisesArray)
print(pushRoutine.targetRepsArray)
print(pushRoutine.targetSetsArray)
print("---------------------------")
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.workoutHistoryArray)
print(testUser.workoutHistoryArray[0].date)
print(testUser.workoutHistoryArray[0].routine.routineName)
print(testUser.workoutHistoryArray[0].note)
print(testUser.workoutHistoryArray[1].date)
print(testUser.workoutHistoryArray[1].routine.routineName)
print(testUser.workoutHistoryArray[1].note)
print("---------------------------")
print(testUser.username)
print(testUser.age)
print(testUser.weight)
print(testUser.personalRoutines[0].routineName)
print(testUser.personalRoutines[0].exercisesArray)
print(testUser.personalRoutines[0].targetRepsArray)
print(testUser.personalRoutines[0].targetSetsArray)
print(testUser.personalRoutines[1].routineName)
print(testUser.personalRoutines[1].exercisesArray)
print(testUser.personalRoutines[1].targetRepsArray)
print(testUser.personalRoutines[1].targetSetsArray)
print("---------------------------")