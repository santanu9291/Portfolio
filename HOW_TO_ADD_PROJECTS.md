#!/usr/bin/env bash
# How to Add More Projects to Your Portfolio

## Current Projects
The portfolio now supports multiple projects easily! Here are the current projects:

1. **Differences Finder** (ID: diff-finder)
   - URL: project-details.html?project=diff-finder

2. **Fruitiya** (ID: fruitiya)
   - URL: project-details.html?project=fruitiya

3. **Card Match Puzzle** (ID: card-match)
   - URL: project-details.html?project=card-match

## How to Add a New Project

### Step 1: Add Project Data
Open `project-details.html` and find the `allProjects` object in the script section.
Add a new project like this:

```javascript
'your-project-id': {
  id: 'your-project-id',
  name: 'Your Project Name',
  shortName: 'Short Name',
  category: 'Project Category',
  description: 'Short description (one line)',
  longDescription: 'Detailed description of your project...',
  features: [
    'Feature 1',
    'Feature 2',
    'Feature 3',
    // ... add more features
  ],
  media: [
    { type: 'image', src: '/path/to/image1.jpg' },
    { type: 'image', src: '/path/to/image2.jpg' },
    { type: 'image', src: '/path/to/image3.jpg' },
  ],
  stats: {
    downloads: '100K+',
    reviews: '5K+',
    rating: 4.5,
    platforms: 'Android, iOS'
  },
  playstore: 'https://play.google.com/store/...',
  appstore: 'https://apps.apple.com/...',
  videoUrl: 'https://www.youtube.com/embed/VIDEO_ID',
  technologies: ['Tech1', 'Tech2', 'Tech3'],
  releaseDate: '2024'
},
```

### Step 2: Add Project to Portfolio
In `index.html`, add a new project card in the projects-grid:

```html
<div class="project-card">
  <div class="project-card-inner">
    <div class="project-image-wrapper">
      <img src="your-image.jpg" alt="Project Name" class="project-img" />
      <div class="project-overlay"></div>
    </div>
    <div class="project-content">
      <div class="project-tag">Category</div>
      <h3>Project Name</h3>
      <p class="project-tech">Tech Stack • Language</p>
      <p class="project-description">Brief description of your project.</p>
      <a href="project-details.html?project=your-project-id" class="project-btn">View Details →</a>
    </div>
  </div>
</div>
```

### Step 3: Add Project Images
1. Create a folder for your project in `/asset/project_media/YourProjectName/`
2. Add your screenshot images (JPG or PNG)
3. Update the `media` array in Step 1 with correct paths

## Example: Adding a "Snake Game" Project

In `project-details.html` script, add:

```javascript
'snake-game': {
  id: 'snake-game',
  name: 'Snake Game Classic',
  shortName: 'Snake',
  category: 'Action Game',
  description: 'A modernized version of the classic snake game with power-ups and multiple levels.',
  longDescription: 'Experience the timeless Snake game reimagined with modern graphics, smooth controls, and challenging gameplay. Collect power-ups, unlock achievements, and compete on the leaderboard.',
  features: [
    '10 difficulty levels',
    'Power-ups and special items',
    'Progressive difficulty',
    'Sound effects and music',
    'High score tracking',
    'Offline gameplay'
  ],
  media: [
    { type: 'image', src: '/asset/project_media/SnakeGame/1.png' },
    { type: 'image', src: '/asset/project_media/SnakeGame/2.png' },
    { type: 'image', src: '/asset/project_media/SnakeGame/3.png' },
  ],
  stats: {
    downloads: '150K+',
    reviews: '4K+',
    rating: 4.3,
    platforms: 'Android, iOS'
  },
  playstore: 'https://play.google.com/store/...',
  appstore: 'https://apps.apple.com/...',
  videoUrl: 'https://www.youtube.com/embed/YOUR_VIDEO_ID',
  technologies: ['Unity', 'C#'],
  releaseDate: '2024'
},
```

In `index.html`, add the project card in the projects-grid section.

## Professional Design Features

✓ Automatic project loading from URL parameters
✓ Professional card design with hover effects
✓ Image slider with smooth animations
✓ Feature accordion that expands/collapses
✓ Gallery with multiple images
✓ Social sharing buttons
✓ Mobile responsive layout
✓ Stats display (downloads, rating, reviews)
✓ Download/Play Store links

## Tips

- Keep descriptions concise and professional
- Use high-quality images (at least 1600x900 for banners)
- Add 3-5 good screenshots per project
- Include a YouTube video link for better engagement
- Fill in accurate stats and platform information
- Use relevant technology tags
- Test on mobile before publishing

All changes are reflected automatically on the project details page!
