def person_lister(f):
    def inner(people):
        # Sort people by age (third element in each person's data)
        people = sorted(people, key=lambda x: int(x[2]))
        # Apply the function `f` to each person and return the result
        return [f(person) for person in people]
    return inner