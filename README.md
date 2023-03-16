
# Astro Pack
This application was created for the course *CSC 394 - Software Projects*, a Senior Capstone course at DePaul University which took over the time span of 1/3/2023 through 3/14/2023.

**Background**\
This project is group based, with group mates chosen by the professor via a survey at the beginning of the course. In the first five weeks of the course, the team brainstormed and researched ideas for an application to create. Most importantly, we had to acknowledge that our application would have to be created in the five weeks after.

As we found, group members all varied in their skills and experience. Furthermore, one thing all members could relate with, is the fact that we were all new to Django. For this, this was the major learning curve that we all had to overcome in the short span of time.

**Purpose of Application**\
One problem that we wanted to help solve is the difficulties that come arise when one plans for a trip. Namely, often times people may not recognize on the spot what item they need to pack for a trip. For this, our team wanted to tackle this problem by making a trip easier for a user by generating a suggested packing list for them. Ideally as the user is packing items, they are referencing our app and checking off the items they already got covered or do not want.

Factors that impact the packing list created are the following: the user's destination, gender, occasion, and activity. 

Alongside creating a packing list for a user's trip, the application also stores the previous trips of a user. With this, the user can revisit the packing list attached to said trip.

Although we acknowledge that other packing list websites/applications exist, we found that they had some issues that we wanted to resolve. For an example, some websites weren't user friendly in its design, others were missing some items one would ideally like to have packed, etc.


**Our Goals and Submission**\
Prior to starting on the project, we had the following five *high level goals* be set as the main goals of our app. Given our limited time frame it wasn't expected to have all five goals be completed upon final submission, but were expected to have completed at least three out of the five. Those five goals are the following:
1. Provide a user-friendly, customizable packing checklist that allows users to easily check off items as they pack and add personal items to the list.
2. Implement a login feature that enables users to save and access their personalized packing lists for future trips.
3. Develop a reminder system that alerts users to repack checklist items before leaving the hotel to prevent forgotten items.
4. Enhance user experience and customization by adding filtering options to the packing list generator.
5. Integrate user recommendations and an Amazon storefront into the app to further assist users with their packing needs.
\
By our final submission on 3/7/2023, we managed to successfully complete the goal #1, #2, and #4. For this, we found ourselves overall satisfied with what we were able to accomplish.

**Future Modifications**\
Following our submission, we'd like to further improve our application with the following:
1.  Complete *high level goal* #3 (see above)
2.  Request for a verification code for a user upon login.
3.  Resolve existing bugs/issues
   - Trip duplication in backend
   - Django error when a new user immediately clicks Current Trip (no trip exists)
   
4.  Minor updates
   - Make Sign Up page more closely match Login page.
   - Update sidebar for Current Trips, Saved Trips, etc.
   - Make Saved Trips have a grid


**Resources**
-
   - **Google Place Autocomplete API**, which is part of the *Google Maps Platform*, was used for the destination field in the dashboard page.
      - The data of interest that is grabbed is the destination name and the latitude & longitude of said destination.
   - The latitude and longitude would then be plugged into the **OpenWeatherMap Weather API** to determine the weather for a user's destination.
      - OpeanWeatherMap is called using fetch API in JavaScript and JSON data is returned for weather.

