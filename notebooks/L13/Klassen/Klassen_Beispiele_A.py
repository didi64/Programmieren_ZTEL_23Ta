# Student
def get_grades(self):
    return {subject: sum(grades)/len(grades) for subject, grades in self.grades.items()}


# Hanoi
# in __init__
self.history = []
# in move_disk
self.history.append((src, dst))

# Vektoren
def __mul__(self, other):
    if isinstance(other, Vec2d):
        return self.x * other.x + self.y * other.y
    else:
        return Vec2d(other*self.x, other*self.y)

def norm(self):
    return (self*self) ** 0.5