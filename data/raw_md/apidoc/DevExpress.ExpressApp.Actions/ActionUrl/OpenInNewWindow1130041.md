---
uid: DevExpress.ExpressApp.Actions.ActionUrl.OpenInNewWindow
name: OpenInNewWindow
type: Property
summary: Specifies whether to load an Action's page in a new window.
syntax:
  content: |-
    [DefaultValue(true)]
    public bool OpenInNewWindow { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if XAF opens the page in a new window; otherwise, `false`.'
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionUrl.UrlFormatString
---

> [!NOTE]
> If the `isDropDown` property of the @DevExpress.ExpressApp.Actions.ActionUrl's Container is set to `true`, XAF ignores the `OpenInNewWindow` property value.