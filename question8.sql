WITH Medians AS (
  SELECT
    country,
    AVG(daily_vaccinations) AS median_daily_vaccinations
  FROM
    country_vaccination_stats
  WHERE
    daily_vaccinations IS NOT NULL
  GROUP BY
    country
)
SELECT
  t.country,
  t.date,
  COALESCE(t.daily_vaccinations, m.median_daily_vaccinations, 0) AS daily_vaccinations
FROM
  country_vaccination_stats t
LEFT JOIN
  Medians m ON t.country = m.country;
