<template>
  <main>
    <h1>Yuval Greenfield</h1>

    <div class="contact">
      <div><a href="mailto:ubershmekel@gmail.com">email</a></div>
      <div><a href="https://bsky.app/profile/ubershmekel.bsky.social">bsky</a></div>
      <div><a href="https://twitter.com/ubershmekel/">twitter</a></div>
      <div><a href="https://www.linkedin.com/in/yuv/">linkedin</a></div>
      <div><a href="https://medium.com/@ubershmekel/">medium</a></div>
      <div><a href="https://github.com/ubershmekel/">github</a></div>
    </div>

    <h2>Projects</h2>
    <div v-for="proj in projects" :key="proj.name" class="project">
      <a :href="proj.link" class="project-name">
        <p class="name">{{ proj.name }}</p>
        <p class="desc">{{ proj.desc }}</p>
        <p class="date">{{ proj.date }}</p>
      </a>
      <hr />
    </div>

    <div>
      The source for this page is at <a
        href="https://github.com/ubershmekel/yuvalg.com">github.com/ubershmekel/yuvalg.com</a>
    </div>
  </main>
</template>

<script lang="ts">
import { ref } from "@vue/composition-api";

export default {
  setup() {
    return {
      // This was projects: ref(projects) for a while
      // But that made no projects render at all at one point.
      // I wonder what that was about.
      projects: projects
    };
  },

  head() {
    return {
      title: "Yuval Greenfield",
      meta: [
        // hid is used as unique identifier. Do not use `vmid` for it as it will not work
        { name: 'description', hid: 'description', content: "What I've been up to" },
      ],
    }
  },
};

const projects = [
  {
    name: "Kat and Noodles - Zensnake",
    desc: "A chill one-button snake game",
    link: "https://ubershmekel.github.io/zensnake/app/",
    date: "2026-01"
  },
  {
    name: "News Since When",
    desc: "A slower news site to catch you up on the top items from the last 30 days",
    link: "https://ubershmekel.github.io/news-analyzer/",
    date: "2025-01"
  },
  {
    name: "Bell Curve Balls (Phaser)",
    desc: "Experiment comparing Godot vs Phaser for web game dev — balls bouncing into a bell curve distribution, built in Phaser",
    link: "https://ubershmekel.github.io/bell-curve-balls/",
    date: "2024-12"
  },
  {
    name: "Bell Curve Balls (Godot)",
    desc: "Experiment comparing Godot vs Phaser for web game dev — balls bouncing into a bell curve distribution, built in Godot",
    link: "https://ubershmekel.github.io/godot-bell-curve-balls/",
    date: "2024-12"
  },
  {
    name: "You Are the Translator",
    desc: "A game to learn a language while you drive",
    link: "https://www.youarethetranslator.com/",
    date: "2023-08"
  },
  {
    name: "Nuke Tech Experiment Labs",
    desc: "A red button game made in 48 hours that tests what kind of reinforcement motivates you",
    link: "https://ubershmekel.github.io/ld51/",
    date: "2022-10"
  },
  {
    name: "I don't know how to code",
    desc: "A card game made in 48 hours about your first software engineering role",
    link: "https://ubershmekel.github.io/ld50/",
    date: "2022-04"
  },
  {
    name: "Unstabable",
    desc: "A game made in 48 hours about earning money by building a tall tower until you reach god",
    link: "https://ubershmekel.github.io/ld49/",
    date: "2021-10"
  },
  {
    name: "Where is Bob?",
    desc: "A game made in 48 hours about an ant climbing a poop pile, finding its friend through a musical radar",
    link: "https://ubershmekel.github.io/ld48/",
    date: "2021-04"
  },
  {
    name: "don't go",
    desc: "A game made in 48 hours. A platformer where you can’t see anything. You have to explore and navigate using your sense of sound",
    link: "https://dontgo.netlify.app/",
    date: "2020-10"
  },
  {
    name: "Egg Rocket Unicorn",
    desc: "A game made in 48 hours for Ludum Dare 46",
    link: "https://ubershmekel.github.io/egg-rocket-unicorn/",
    date: "2020-04"
  },
  {
    name: "Building Products People Love",
    desc:
      "Online meetup for sharing product design lessons from Notion, Uber and General Magic",
    link: "https://www.meetup.com/Samsung-NEXT/events/268868032/",
    date: "2020-04"
  },
  {
    name: "Cook Magic",
    desc: "Text messaging Slack bot that searches for recipes",
    link: "https://www.producthunt.com/posts/cook-magic",
    date: "2020-04"
  },
  {
    name: "Internet Leaderboard",
    desc: "The top trending content from reddit, YouTube, and Twitter",
    link: "https://www.internetleaderboard.com",
    date: "2020-01"
  },
  {
    name: "dick-butt-fractal",
    desc: "Fractal animation experiment with JavaScript",
    link: "https://ubershmekel.github.io/dick-butt-fractal/",
    date: "2020-01"
  },
  {
    name: "WebCard",
    desc: "Make a bookmark to use as a digital business card",
    link: "https://ubershmekel.github.io/webcard/",
    date: "2019-11"
  },
  {
    name: "How AI is Changing the World",
    desc:
      "Series of events in 4 cities with AI expert talks from Google, Uber, Giphy, and more",
    link: "https://samsungnext.com/whats-next/how-is-ai-changing-the-world/",
    date: "2019-10"
  },
  {
    name: "vocal-warm-up-js",
    desc:
      "JavaScript generated audio for a configurable vocal warm up exercise",
    link: "https://ubershmekel.github.io/vocal-warm-up-js/",
    date: "2019-10"
  },
  {
    name: "Tagsyo",
    desc: "Use SQL to query what's trending on YouTube, Reddit, Instagram, and Twitter",
    link: "https://www.tagsyo.com/",
    date: "2019-07"
  },
  {
    name: "CSS Bed",
    desc: "Test bed for simple CSS resets that make your static page nice, without using classes",
    link: "https://www.cssbed.com/",
    date: "2019-05"
  },
  {
    name: "movie2cal",
    desc: "Create a calendar event for a movie premiere",
    link: "https://ubershmekel.github.io/movie2cal/",
    date: "2019-01"
  },
  {
    name: "precision-recall-f1",
    desc:
      "An interactive representation of machine learning metrics like sensitivity, precision, recall, and specificity",
    link: "https://ubershmekel.github.io/precision-recall-f1/",
    date: "2018-10"
  },
  {
    name: "experimenter",
    desc:
      "Zero latency AB testing snippet using Google Analytics or Facebook pixel events",
    link: "https://github.com/ubershmekel/experimenter",
    date: "2017-11"
  },
  {
    name: "fps-vis",
    desc:
      "Python script to generate a visual comparison of 15, 30, and 60 fps animations",
    link: "https://github.com/ubershmekel/fps-vis",
    date: "2017-10"
  },
  {
    name: "pinglog",
    desc:
      "Python script to schedule and log ping results in an sqlite database",
    link: "https://github.com/ubershmekel/pinglog",
    date: "2017-10"
  },
  {
    name: "twitchn",
    desc:
      "Show the most popular Twitch streams for a given game, eg for a game studio cafeteria",
    link: "https://github.com/ubershmekel/twitchn",
    date: "2016-04"
  },
  {
    name: "gfilter",
    desc: "Drag in a csv to get an interactive cross filter dashboard",
    link:
      "https://ubershmekel.github.io/gfilter/?dl=testData/TechCrunchcontinentalUSA.csv",
    date: "2016-04"
  },
  {
    name: "Balls vs Blocks",
    desc: "Desktop web physics game to knock down blocks with your balls",
    link:
      "http://ubershmekel.github.io/ballsvsblocks/",
    date: "2016-03"
  },
  {
    name: "Mine3js",
    desc:
      "WebGL minecraft that stores the blocks placed in the URL so you can share your creation",
    link: "https://ubershmekel.github.io/mine3js/",
    date: "2013-05"
  },
  {
    name: "redditp",
    desc:
      "Turn any reddit url to a slideshow. Gets a million page views a month",
    link: "https://redditp.com/",
    date: "2012"
  },
  {
    name: "Python3WOS",
    desc: "Status chart of Python packages migration from Python 2 to 3",
    link: "https://web.archive.org/web/20200218173018/https://python3wos.appspot.com/",
    date: "2011-02"
  },
  {
    name: "freeball",
    desc: "Multiplayer WebGL flying soccer ball game",
    link: "https://ubershmekel.github.io/freeball/",
    date: "2011-02"
  },

  {
    name: "WordPress blog",
    desc: "Mostly Python and Android blog, now defunct",
    link: "https://uberpython.wordpress.com/",
    date: "2008-2013"
  },

  {
    name: "Top Less Productions",
    desc: "Award winning 48 hour film production team",
    link:
      "https://www.youtube.com/user/TopLessProd/videos?view=0&sort=p&flow=grid",
    date: "2008-2013"
  },
  {
    name: "Pendulum Waves",
    desc: "WebGL experiment with a trippy rhythm",
    link: "https://toplessproductions.github.io/pendulum/",
    date: "2008-2013"
  },
  {
    name: "Traitsim",
    desc:
      "Visualization to show that recessive genes aren't more likely to go extinct",
    link: "http://ubershmekel.github.io/traitsim/",
    date: "2012-10"
  },
  {
    name: "filecache",
    desc: "Python decorator for caching function calls to disk",
    link: "https://pypi.org/project/filecache/",
    date: "2011-02"
  },
  {
    name: "biotet",
    desc: "Circular tetris flex (flash) game",
    link: "https://toplessproductions.github.io/biotet/",
    date: "2011-01"
  }
];
</script>

<style>
html {
  /* background-color: #3f0082; */
  background: rgb(16, 0, 16);
  background: linear-gradient(179deg, rgba(32, 4, 111, 1) 0%, rgba(57, 9, 73, 1) 50vh, rgba(16, 0, 16, 1) 100vh, rgba(32, 4, 111, 1) 100%);

  min-height: 100%;

  color: #f2f;
  /* text-shadow: 2px 2px 5px #ff2975; */
  text-shadow: 2px 2px 10px #c0c;

  /* deny horizontal scroll bars */
  overflow-x: hidden;
}

body {
  font-family: monospace, 'Inconsolata';
}

h1 {
  /* font-size: 1.5em; */
  /* font-size: 2.5vw; */
  font-size: 3em;
}

h2 {
  font-size: 2em;
}

.contact {
  /* font-size: 2.5vw; */
  font-size: 2em;
}

.contact div {
  display: block;
}

a {
  text-decoration: none;
  color: #ffeb3b;
  transition: color 0.5s;
}

a:hover {
  color: #f90;
}

.desc,
.date {
  color: #edf;
  text-shadow: 0px 0px 10px rgb(157, 216, 255);
  font-size: 1rem;
}

hr {
  background: linear-gradient(to right, rgba(255, 255, 255, 0) 0px, #9df 100px, rgba(0, 0, 0, 0) 300px);
  height: 2px;
  border: none;
  transition: background 0.3s;
}

main {
  position: relative;
}

.project {
  position: relative;
}

.project:hover {
  background: rgba(255, 255, 255, 0.1);
  transition: background 0.3s;
}
</style>
