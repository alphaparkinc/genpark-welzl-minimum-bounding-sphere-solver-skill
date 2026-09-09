import math
import random

class WelzlBoundingSphereSolver:
    """Welzl's exact linear-time O(N) minimum enclosing ball solver."""
    def _dist(self, p1, p2) -> float:
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

    def _ball_from_2pts(self, p1, p2) -> tuple[tuple[float, ...], float]:
        center = tuple((a + b) / 2.0 for a, b in zip(p1, p2))
        radius = self._dist(p1, p2) / 2.0
        return center, radius

    def _ball_from_3pts_2d(self, p1, p2, p3) -> tuple[tuple[float, float], float]:
        # Circumcenter of triangle
        d = 2 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]))
        if abs(d) < 1e-9:
            return self._ball_from_2pts(p1, p2)
        ux = ((p1[0]**2 + p1[1]**2)*(p2[1] - p3[1]) + (p2[0]**2 + p2[1]**2)*(p3[1] - p1[1]) + (p3[0]**2 + p3[1]**2)*(p1[1] - p2[1])) / d
        uy = ((p1[0]**2 + p1[1]**2)*(p3[0] - p2[0]) + (p2[0]**2 + p2[1]**2)*(p1[0] - p3[0]) + (p3[0]**2 + p3[1]**2)*(p2[0] - p1[0])) / d
        center = (ux, uy)
        return center, self._dist(center, p1)

    def solve(self, points: list[tuple[float, float]]) -> dict:
        if not points:
            return {"center": (), "radius": 0.0}
        if len(points) == 1:
            return {"center": points[0], "radius": 0.0}

        pts = list(points)
        random.seed(42)
        random.shuffle(pts)

        # Base case
        center, radius = self._ball_from_2pts(pts[0], pts[1])

        for i in range(2, len(pts)):
            if self._dist(center, pts[i]) > radius + 1e-7:
                center, radius = pts[i], 0.0
                for j in range(i):
                    if self._dist(center, pts[j]) > radius + 1e-7:
                        center, radius = self._ball_from_2pts(pts[i], pts[j])
                        for k in range(j):
                            if self._dist(center, pts[k]) > radius + 1e-7:
                                center, radius = self._ball_from_3pts_2d(pts[i], pts[j], pts[k])

        return {
            "num_points": len(points),
            "center": tuple(round(c, 4) for c in center),
            "radius": round(radius, 4)
        }
