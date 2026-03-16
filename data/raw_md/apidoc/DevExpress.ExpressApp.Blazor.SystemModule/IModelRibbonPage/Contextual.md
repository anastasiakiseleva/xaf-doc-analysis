---
uid: DevExpress.ExpressApp.Blazor.SystemModule.IModelRibbonPage.Contextual
name: Contextual
type: Property
summary: Specifies whether the current ribbon page is highlighted.
syntax:
  content: |-
    [DefaultValue(false)]
    bool Contextual { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if the page is contextual; otherwise, `false`.'
seealso: []
---
The XAF application shows ribbon pages when they have visible actions. Contextual ribbon pages (where `Contextual` is `true`) are highlighted and appear after standard ribbon pages.

![Context Ribbon Page](~/images/xaf-blazor-ribbon-page-context.png)
