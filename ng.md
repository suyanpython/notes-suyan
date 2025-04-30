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
// app.routes
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

// app.config

import {provideRouter} from '@angular/router';
import {routes} from './app.routes';
export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes)],
};

// if not reload entire page, import RouterLink and change href into RouterLink in html
```

# Syntactic sugar 
```
this.theme.update(currentValue => currentValue === 'light' ? 'dark' : 'light');
```
