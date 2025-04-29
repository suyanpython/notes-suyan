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
