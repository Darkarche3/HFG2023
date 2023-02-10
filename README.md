# HFG2023
Repository containing code used in the Hack For Good 2023 Hackathon organised by DSC @ NUS Computing.

Special thanks to my collaborators, **Suraj Bantwal, Chin Yan Xu, and Teo Hui Qian**, for bringing this project to life.

You may follow along with a demo of this website at https://youtu.be/YJfrbkQapUM

# How To Access 
The main project folder can be found in **u4g_projects_page_final.zip**. Set the directory of your local terminal to the extracted folder and run the command

`python manage.py runserver`

Ctrl + Click the development server hyperlink generated to access the index page.
From there, one can proceed to explore the projects, profile, and collaborations pages. To access the sign-up page, add "/signup" to the back of the index website URL. To access the admin panel, replace `"/projects"` with `"/admin"` in the website's URL. To login, one can use the credentials below:

`User: h4g2023`
`Pass: unicornsforgood`

# Project Description
Global Connect is a **one-stop projects crowdsourcing repository**, enabling registered companies to share social initaitives that they are organising and garner partners and participants.  Projects are displayed in a list format, organised by categories. Signing up is fast and straightforward, and participants can easily reach out to organisers via email to enquire more about specific projects of interest. Drawing together a wide variety of companies, each is able to contribute resources and skills from their field of expertise to help **"solve each other's problems"** and execute successful projects that affect real change to their target beneficiaries.

#Projects, Profiles, User Authentication
Visitors can register for projects they would like to contribute to at the bottom of the respective pages. Their particulars are saved into the website's in-built admin system, which stores information on all projects, participants, categories and locations currently hosted on the server. Prior user authentication ensures that only registered members can sign up for projects.

# Collaborations

Our key feature is the **collaborations page**, where a visitor can see at a glance **all shared projects** between any two parties. This is useful in enabling companies to keep track of all ongoing partnerships, identify companies with whom they share many common goals with, and even extend invitations to those they would not have noticed otherwise. Individual profile pages also enable visitors to learn more about a company's available projects, areas of business, and past collaborations.

# Admin Panel
From the admin panel, one can **view all existing projects, participants, and categories.** **CRUD operations can be performed seamlessly** and immediately refleccted on the site. Social Innovation Park is thus able to manage and follow up with registered participants and companies, as well as ensure that crucial project details and information is not compromised or stolen.

# Conclusion

Together, the Global Connect website offers a strong starting point for **building a tech-for-good ecosystem to explore innovative social initiatives that span across multiple disciplines, and foster collaborations across all registered members**, making the site a platform of choice for any company hoping to make a difference in the lives of the underprivileged.
