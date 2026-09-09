from client import WelzlBoundingSphereSolver

def main():
    print("=== Welzl Minimum Enclosing Ball Solver ===")
    solver = WelzlBoundingSphereSolver()

    # Square with vertices at (0,0), (4,0), (4,4), (0,4)
    square_pts = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0), (2.0, 2.0)]
    res = solver.solve(square_pts)
    print("Minimum Enclosing Ball:", res)
    assert res["center"] == (2.0, 2.0)
    assert abs(res["radius"] - 2.8284) < 1e-3

    print("Welzl Bounding Sphere Solver verified successfully!")

if __name__ == "__main__":
    main()
