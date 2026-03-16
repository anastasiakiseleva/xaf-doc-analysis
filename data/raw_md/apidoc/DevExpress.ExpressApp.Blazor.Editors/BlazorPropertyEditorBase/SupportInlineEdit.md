---
uid: DevExpress.ExpressApp.Blazor.Editors.BlazorPropertyEditorBase.SupportInlineEdit
name: SupportInlineEdit
type: Property
summary: Specifies whether the Property Editor is displayed in read-only mode when its used for in-line editing in a Grid List Editor.
syntax:
  content: public virtual bool SupportInlineEdit { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` to display the Property editor in edit mode; otherwise, `false`.'
seealso: []
---
A Grid List Editor generates Property Editors when you allow in-line editing.  When you create a custom editor, the Grid List Editor can display them in read-only mode. You can set the `SupportInlineEdit` propety to `false` to disable this behavior.
