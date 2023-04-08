function generateResumeView(experiences) {
    const starredExperiences = experiences.filter((experience) => experience.starred);
    const sortedStarredExperiences = starredExperiences.sort((a, b) => Math.max(...b.years) - Math.max(...a.years));  
  
    let html = "<ul>";
    sortedStarredExperiences.forEach((experience) => {
      const minYear = Math.min(...experience.years);
      const maxYear = Math.max(...experience.years);
      const years = minYear === maxYear ? `(${minYear})` : `(${minYear} - ${maxYear})`;
      const skills = experience.skills.join(", ");
      html += `<li><p><strong>${experience.name}</strong> ${years} -- ${experience.description}`;
      if (experience.link) {
        html += ` (<a href="${experience.link}">Link</a>)`;
      }
      html += ` -- ${skills}</p></li>`;
    });
    html += "</ul>";
  
    return html;
  }

  function generateTimelineView(experiences) {
    const sortedExperiences = experiences.sort((a, b) => Math.max(...b.years) - Math.max(...a.years));
  
    let html = "<ul>";
    sortedExperiences.forEach((experience) => {
      const minYear = Math.min(...experience.years);
      const maxYear = Math.max(...experience.years);
      const years = minYear === maxYear ? `${minYear}` : `${minYear} - ${maxYear}`;
  
      html += `<li><p><strong>${years}</strong> -- ${experience.name} -- ${experience.description}`;
      if (experience.link) {
        html += ` (<a href="${experience.link}">Link</a>)`;
      }
    });
    html += "</ul>";
  
    return html;
  }

function generateSkillsView(experiences) {
    const skillsMap = new Map();
  
    experiences.forEach((experience) => {
      if (!experience.skills) return;
      experience.skills.forEach((skill) => {
      if (!skillsMap.has(skill)) {
        skillsMap.set(skill, []);
      }
      skillsMap.get(skill).push(experience);
    });
  });

  const sortedSkills = Array.from(skillsMap.keys()).sort((a, b) => skillsMap.get(b).length - skillsMap.get(a).length);

  let html = "<ul>";
  sortedSkills.forEach((skill) => {
    const relatedExperiences = skillsMap.get(skill);
    html += `<li><p><strong>${skill}</strong>: `;
    relatedExperiences.forEach((experience, index) => {
      if (experience.link) {
        html += `<a href="${experience.link}">${experience.name}</a>`;
      } else {
        html += experience.name;
      }
      if (index < relatedExperiences.length - 1) {
        html += "; ";
      }
    });
    html += "</p></li>";
  });
  html += "</ul>";

  return html;
}

function generateCVView(experiences) {
    const filteredExperiences = experiences.filter((experience) => experience.type !== "Work");
    const typeOrder = ["Classes", "Projects", "Publications", "Volunteering", "Work", "Awards"];
    const typeMap = new Map();
  
    filteredExperiences.forEach((experience) => {
      if (!typeMap.has(experience.type)) {
        typeMap.set(experience.type, []);
      }
      typeMap.get(experience.type).push(experience);
    });
  
    const sortedTypes = typeOrder.filter((type) => typeMap.has(type));
  
    let html = "<ul>";
    sortedTypes.forEach((type) => {
      const experiencesByType = typeMap.get(type).sort((a, b) => Math.max(...b.years) - Math.max(...a.years));
  
      html += `<li><p><strong>${type}</strong></p>`;
      html += "<ul>";
  
      experiencesByType.forEach((experience) => {
        const minYear = Math.min(...experience.years);
        const maxYear = Math.max(...experience.years);
        const years = minYear === maxYear ? `${minYear}` : `${minYear} - ${maxYear}`;
        html += `<li><p>${years} -- ${experience.name}`;
        if (experience.link) {
          html += ` (<a href="${experience.link}">Link</a>)`;
        }
        html += `</p></li>`;
      });
  
      html += "</ul></li>";
    });
    html += "</ul>";
  
    return html;
  }

function changeButtonColor(selectedBtn) {
    const buttons = ["resumeBtn", "timelineBtn", "skillsBtn", "cvBtn"];
    buttons.forEach((button) => {
        if (button === selectedBtn) {
        document.getElementById(button).style.backgroundColor = "#00b3e5";
        document.getElementById(button).style.color = "white";
        } else {
        document.getElementById(button).style.backgroundColor = "";
        document.getElementById(button).style.color = "";
        }
    });
}
  

document.getElementById("resumeBtn").addEventListener("click", () => {
  document.getElementById("container").innerHTML = generateResumeView(experiences);
  changeButtonColor("resumeBtn");
});

document.getElementById("timelineBtn").addEventListener("click", () => {
  document.getElementById("container").innerHTML = generateTimelineView(experiences);
  changeButtonColor("timelineBtn");
});

document.getElementById("skillsBtn").addEventListener("click", () => {
  document.getElementById("container").innerHTML = generateSkillsView(experiences);
  changeButtonColor("skillsBtn");
});

document.getElementById("cvBtn").addEventListener("click", () => {
    document.getElementById("container").innerHTML = generateCVView(experiences);
    changeButtonColor("cvBtn");
});

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("container").innerHTML = generateResumeView(experiences);
    changeButtonColor("resumeBtn");
  });