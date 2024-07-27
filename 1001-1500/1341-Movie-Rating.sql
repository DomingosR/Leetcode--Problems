(SELECT       name AS results
FROM         (SELECT       Users.name, COUNT(MovieRating.rating) AS ratingCount
              FROM         Users
              JOIN         MovieRating
              ON           Users.user_id = MovieRating.user_id
              GROUP BY     Users.name
              ORDER BY     ratingCount DESC, Users.name ASC) AS CountRatings
LIMIT         1)
UNION         ALL
(SELECT      title AS results
FROM         (SELECT        Movies.title, AVG(MovieRating.rating) AS AvgRating
              FROM          Movies
              JOIN          MovieRating
              ON            Movies.movie_id = MovieRating.movie_id
              WHERE         MovieRating.created_at < "2020-03-01"
              AND           MovieRating.created_at > "2020-01-31"
              GROUP BY      Movies.title
              ORDER BY      AvgRating DESC, title) AS AverageRating
LIMIT         1);