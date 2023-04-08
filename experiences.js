const experiences = [
    {
        years: [2022, 2023],
        name: "Operations Manager, BibleProject",
        description: "Working with COO on strategy, operating model, organization structure, data and insights",
        skills: ["strategy & operations", "Looker", "Heap", "business intelligence", "Gsuite"],
        link: "https://www.bibleproject.com",
        starred: true,
        type: "Work",
    },

    {
        years: [2023],
        name: "BibleProject Podcast Chatbot",
        description: "An AI-powered chatbot based off a favorite podcast",
        skills: ["Python", "React", "Flask", "GPT"],
        starred: false,
        type: "Projects",
        link: "https://ben-d-t.github.io/bp-podcast-chatbot/",
    },

    {
        years: [2015, 2016, 2017, 2018, 2019],
        name: "Student, University of Virginia",
        description: "Economics and math degree with highest distinction. Lawn resident",
        skills: ["research", "economics", "math"],
        starred: true,
        type: "Education",
    },

    {
        years: [2021, 2022],
        name: "Fellow, McKinsey Global Institute",
        description: "Rotation in McKinsey’s business and economics research think tank",
        skills: ["research", "Powerpoint", "Excel", "Tableau"],
        starred: true,
        type: "Work",
        link: "https://www.mckinsey.com/mgi/overview",
      },

      {
        years: [2018, 2019, 2020, 2021],
        name: "Senior Business Analyst, McKinsey & Company",
        description: "Supported public and private sector organizations on topics at the intersection of economic development and real estate",
        skills: ["economic development", "real estate", "strategic planning", "consulting", "Powerpoint", "Excel"],
        starred: true,
        type: "Work",
      },
      {
        years: [2016, 2017, 2018, 2019],
        name: "Undergraduate Teaching Fellow, UVA Department of Economics",
        description: "Taught 200+ students over 3 years leading two 50-minute discussion sections each week for Principles of Economics",
        skills: ["teaching", "economics"],
        starred: true,
        type: "Work",
      },
      {
        years: [2017, 2018, 2019],
        name: "Research Assistant, UVA Department of Economics",
        description: "Worked with three professors on topics from public policy to international trade",
        skills: ["research", "public policy", "international trade"],
        starred: true,
        type: "Work",
      },
      {
        years: [2019],
        name: "Pro-Bono Consultant, Pathways",
        description: "Digitized check-in process for homeless ministry to speed entry and preserve 10 years of hand-recorded data",
        skills: ["consulting", "data management"],
        starred: false,
        type: "Volunteering",
      },
      {
        years: [2016, 2017, 2018, 2019],
        name: "Team Leader, Young Life Capernaum",
        description: "Led a team of 5 to plan biweekly clubs and other events for high school students with disabilities",
        skills: ["leadership", "event planning"],
        starred: true,
        type: "Volunteering",
      },
      {
        years: [2018, 2019],
        name: "Teacher’s Aide, Albemarle Post High",
        description: "Assisted teachers in specialized school for adults with disabilities by leading life-skills, cooking, and reading classes",
        skills: ["teaching", "assistance"],
        starred: false,
        type: "Volunteering",
      },
      {
        years: [2019, 2020, 2021],
        name: "The Geopolitics of International Trade in Southeast Asia",
        description: "Simulates the impact of potential conflict in the South China Sea to estimate the effects on trade and welfare. Published in the Review of World Economics, February 2021",
        skills: ["trade", "geopolitics", "Python", "QGIS", "Latex", "Matlab", "Stata"],
        starred: false,
        link: "https://link.springer.com/article/10.1007/s10290-020-00403-0",
        type: "Publications",
      },

      {
        years: [2018, 2019],
        name: "The Economic Benefit of the Freedom of the Seas",
        description: "Thesis estimating counterfactual trade flows when key maritime trade passages (e.g., Panama, Suez Canals) are impassable",
        skills: ["research", "QGIS", "Python", "Latex", "Stata", "Matlab", "trade", "geopolitics"],
        starred: false,
        link: "https://ben-d-t.github.io/free-seas",
        type: "Publications",
      },

      {
        years: [2018],
        name: "Political Influence and the Federal Trade Commission (with A. Danel)",
        description: "Received research grant to study congressional influence on FTC decision making in antitrust cases",
        skills: ["research", "political influence", "antitrust", "Python"],
        starred: false,
        link: "https://issuu.com/theoculus/docs/oculus_2018-19",
        type: "Publications",
      },
      {
        years: [2018],
        name: "The Effects of Low Income Housing Assistance on Housing Consumption Patterns",
        description: "Analyzed large administrative dataset to determine how housing programs influence housing choices of recipients",
        skills: ["housing", "Stata"],
        starred: false,
        type: "Publications",
      },
      {
        years: [2017, 2018],
        name: "A Cost-Effective Approach to Improving Low Income Housing Assistance",
        description: "Received research grant to study how mobility assistance affects outcomes for recipients of housing vouchers",
        skills: ["housing", "research", "Stata"],
        starred: false,
        type: "Publications",
      },
      {
        years: [2019],
        name: "Phi Beta Kappa",
        description: "",
        skills: [],
        starred: false,
        type: "Awards",
      },
      {
        years: [2019],
        name: "Duncan Clark Hyde Outstanding Economics Major Award",
        description: "",
        skills: [],
        starred: false,
        type: "Awards",
      },
      {
        years: [2019],
        name: "Outstanding Thesis Prize",
        description: "",
        skills: [],
        starred: false,
        type: "Awards",
      },
      {
        years: [2018],
        name: "Kenneth G. Elzinga Scholarship for Academic Excellence",
        description: "",
        skills: [],
        starred: false,
        type: "Awards",
      },

      {
        years: [2011, 2015],
        name: "Student, Alexandria City HS",
        description: "Valedectorian, Class Speaker",
        type: "Education",
      },

      {
        years: [2017, 2019],
        name: "Caretaker, Public Partnerships",
        description: "State of Virginia program supporting teens and adults with disabilities",
        type: "Work",
      },

      {
        years: [2017],
        name: "Harrison Undergraduate Research Award",
        description: "Grant for research project on housing assistance",
        type: "Awards"
      },

      {
        years: [2016],
        name: "Camp Store Director, Summer Camp",
        type: "Work",
        description: "Oversaw daily operation of camp store, which contributes over $10,000 to operating budget of the camp",

      },

      {
        years: [2019],
        name: "Summer Staff, Young Life",
        type: "Volunteering",
        description: "",
      }, 

      {
        years: [2021],
        name: "The economic state of Black America: What is and what could be (contributor)",
        link: "https://www.mckinsey.com/featured-insights/diversity-and-inclusion/the-economic-state-of-black-america-what-is-and-what-could-be/",
        type: "Publications",
        description: "MGI Report",
      },

      {
       years: [2021],
       name: "The economic state of Latinos in America: The American dream deferred (contributor)",
       link: "https://www.mckinsey.com/featured-insights/sustainable-inclusive-growth/the-economic-state-of-latinos-in-america-the-american-dream-deferred#/",
       type: "Publications",
       description: "McKinsey Article" 
      },

      {
        years: [2022],
        name: "The net-zero transition: What it would cost, what it could bring (contributor)",
        link: "https://www.mckinsey.com/capabilities/sustainability/our-insights/the-net-zero-transition-what-it-would-cost-what-it-could-bring",
        type: "Publications",
        description: "MGI Report",
      }, 

      {
        years: [2022],
        name: "Toward a sustainable, inclusive, growing future: The role of business (contributor)",
        link: "https://www.mckinsey.com/featured-insights/sustainable-inclusive-growth/toward-a-sustainable-inclusive-growing-future-the-role-of-business",
        type: "Publications",
        description: "MGI Discussion Paper",
      },

      {
        years: [2021],
        name: "The case for inclusive growth (contributor)",
        link: "https://www.mckinsey.com/industries/public-and-social-sector/our-insights/the-case-for-inclusive-growth#/",
        description: "McKinsey Article",
        type: "Publications",
      },

      {
        years: [2022],
        name: "Advent of Code",
        description: "My solutions for Eric Wastl's Advent of Code",
        link: "https://ben-d-t.github.io/adventcode-2022",
        type: "Projects",

      },

      {
        years: [2023],
        name: "3D Game of Life",
        description: "An implementation of Conways' GoL wrapped around a cube",
        type: "Projects",
        link: "https://ben-d-t.github.io/3d-game-of-life",
        skills: ["HTML", "CSS", "Javascript"]
      },

      {
        years: [2023],
        name: "Roblox - First team to 1B",
        description: "A simple game in Roblox where two teams try to get to 1 billion points first, using a unique global score sync",
        skills: ["Lua"],
        link: "https://www.roblox.com/games/12922290087/First-team-to-1B-wins",
        type: "Projects",
      },

      {
        years: [2022],
        name: "Codecademy Full Stack Developer Course",
        description: "",
        skills: ["HTML", "Javascript", "CSS", "Python"],
        type: "Education",
      },

      {
        years: [2022],
        name: "Introduction to the Hebrew Bible - BibleProject Classroom",
        description: "Develop skills for reading ancient biblical texts as the authors intended",
        skills: ["hebrew bible"],
        type: "Education",
        link: "https://bibleproject.com/classroom/overview/hebrew-bible-full-class/",
      },

      {
        years: [2023],
        name: "Adam to Noah - BibleProject Classrom",
        description: "Explore Genesis 2-5 to discover the repeating themes that develop throughout Scripture",
        skills: ["hebrew bible", "Genesis"],
        type: "Education",
        link: "https://bibleproject.com/classroom/overview/adam-noah/",
      }

];