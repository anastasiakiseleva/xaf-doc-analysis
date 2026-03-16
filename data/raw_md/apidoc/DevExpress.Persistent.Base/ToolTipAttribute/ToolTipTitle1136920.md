---
uid: DevExpress.Persistent.Base.ToolTipAttribute.ToolTipTitle
name: ToolTipTitle
type: Property
summary: Specifies the tooltip title. Has effect in XAF Windows Forms applications only.
syntax:
  content: public string ToolTipTitle { get; }
  parameters: []
  return:
    type: System.String
    description: The tooltip title.
seealso: []
---
> [!IMPORTANT]
> This property is in effect in XAF Windows Forms applications only.

Use @DevExpress.Persistent.Base.ToolTipAttribute.ToolTipTitle and @DevExpress.Persistent.Base.ToolTipAttribute.ToolTipIconType properties to specify a title and an icon for a tooltip. These elements are displayed in editor and layout item tooltips in Detail View.

```csharp
[ToolTip("When this option is checked, it overrides all other permission settings and grants full access to all operations.",
    "Specifies whether associated users are administrators.",ToolTipIconType.Information)]
public virtual bool IsAdministrative { get; set; }
```

![TooltipAdvanced_Win](~/images/tooltipadvanced_win117182.png)