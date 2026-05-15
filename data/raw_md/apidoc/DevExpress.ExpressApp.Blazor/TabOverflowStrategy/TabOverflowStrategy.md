---
uid: DevExpress.ExpressApp.Blazor.TabOverflowStrategy
name: TabOverflowStrategy
type: Enum
summary: Lists values that specify how to handle overflowing tabs.
syntax:
  content: public enum TabOverflowStrategy
seealso: []
---
`UnloadLeastRecentTab` and `CloseLeastRecentTab` strategies do not unload or close tabs with unsaved changes. The total tab count may temporarily exceed the limit if the oldest tabs are being modified.