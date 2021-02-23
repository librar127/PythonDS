CREATE PROCEDURE placesOfInterest()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    select
        country,
        sum(case when leisure_activity_type="Adventure park" then number_of_places else 0 end) as adventure_park,
        sum(case when leisure_activity_type="Golf" then number_of_places else 0 end) as Golf,
        sum(case when leisure_activity_type="River cruise" then number_of_places else 0 end) as river_cruise,
        sum(case when leisure_activity_type="Kart racing" then number_of_places else 0 end) as kart_racing
    FROM
        countryActivities
    group BY
        country
    order BY
        country;
END