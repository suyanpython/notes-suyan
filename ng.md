✅ Example using @for (Angular 17+)
In a standalone component:
```
@for (item of items; track item.id) {
  <div>{{ item.name }}</div>
}
```

🔄 With Index
```
<li *ngFor="let item of items; let i = index">
  {{ i }} - {{ item }}
</li>
```
🔄 With keyvalue for objects
```
<div *ngFor="let entry of info | keyvalue">
  {{ entry.key }}: {{ entry.value }}
</div>
```

# Component-level Lazy Loading
```
@defer {
  <comments />
} @placeholder {
  <p>Comments will appear once you scroll here</p>
} @loading {
  <p>Loading comments...</p>
} @error {
        <p>Failed to load comments</p>
 }

```

# Image optimization 
- import {NgOptimizedImage} from '@angular/common';
- add width height
- Dynamic / static images

  # Routes
- in app.component: import {RouterOutlet} from '@angular/router';
- add app.routes
- edit app.config

```
// app.routes.ts
import {Routes} from '@angular/router';
export const routes: Routes = [ {
    path: '',
    title: 'App Home Page',
    component: HomeComponent,
  },
  {
    path: 'user',
    title: 'App User Page',
    component: UserComponent,
  },
];


// main.ts inline way of adding routes
// main.config.ts or app.config.ts  to be imported in main.ts, you can add other configs such as Zone (best practice)
// or you name it environment.ts  for build-time config

import {provideRouter} from '@angular/router';
import {routes} from './app.routes';
export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes)],
};

// if not reload entire page, import RouterLink and change href into RouterLink in html
add import { RouterModule } from '@angular/router';

//globally
replace:
<app-home></app-home>
into:
<router-outlet></router-outlet>
```

# Syntactic sugar 
```
this.theme.update(currentValue => currentValue === 'light' ? 'dark' : 'light');

//in Templates, If exists, use its photo property for the image src; otherwise, don’t throw an error
housingLocation?.photo

```
# Json DB for local testing 

- npm install -g json-server
- json-server --watch db.json

# npm install	VS npm ci

# Best pratices : 
```
// use variable for base url
const API_BASE_URL = process.env.API_BASE_URL;
fetch(`${API_BASE_URL}/posts`);

//clean up resources
useEffect(() => {
  window.addEventListener('resize', handleResize);
  return () => window.removeEventListener('resize', handleResize);
}, []);

```
# Standalone 
- ng new my-app --standalone
- bootstrapApplication(...) in main.ts



## DOM Event Bindings in Angular

### Mouse Events
- `(click)="..."`
- `(dblclick)="..."`
- `(mousedown)="..."`
- `(mouseup)="..."`
- `(mouseenter)="..."`
- `(mouseleave)="..."`
- `(mousemove)="..."`
- `(contextmenu)="..."`

### Keyboard Events
- `(keydown)="..."`
- `(keyup)="..."`
- `(keypress)="..."`

### Form/Input Events
- `(input)="..."`
- `(change)="..."`
- `(focus)="..."`
- `(blur)="..."`
- `(submit)="..."`

### Clipboard Events
- `(copy)="..."`
- `(cut)="..."`
- `(paste)="..."`

### Drag & Drop Events
- `(drag)="..."`
- `(dragstart)="..."`
- `(dragend)="..."`
- `(dragenter)="..."`
- `(dragleave)="..."`
- `(dragover)="..."`
- `(drop)="..."`

### Touch Events
- `(touchstart)="..."`
- `(touchend)="..."`
- `(touchmove)="..."`

### Media Events
- `(play)="..."`
- `(pause)="..."`
- `(ended)="..."`
- `(timeupdate)="..."`

### Window Events
- `(window:resize)="..."`
- `(window:scroll)="..."`

### Custom Events
- `(myCustomEvent)="..."`

# Tailwind 
- npm install -D tailwindcss postcss autoprefixer
- npx tailwindcss init -p
  
- tailwind.config.js

  
  `
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
} 
  `


- postcss.config.js

```
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```


- styles.css

```
@tailwind base;
@tailwind components;
@tailwind utilities;
```


- package.json

```
"scripts": {
  "build:tailwind": "npx tailwindcss -i ./src/styles.css -o ./dist/styles.css --watch",
  "build:prod:tailwind": "npx tailwindcss -i ./src/styles.css -o ./dist/styles.min.css --minify",
  // ... other scripts
}
```

- Include the generated CSS in your angular.json:
Make sure the output CSS file (./dist/styles.css or ./dist/styles.min.css) is included in the styles array of your build configuration.
