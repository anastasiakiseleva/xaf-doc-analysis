---
uid: DevExpress.ExpressApp.Actions.ActionBase.DiagnosticInfo
name: DiagnosticInfo
type: Property
summary: Specifies information on an Action. This information is appended to the information on the remaining Actions and their [Controllers](xref:112621) and displayed via the **DiagnosticInfo** Action.
syntax:
  content: |-
    [Browsable(false)]
    public string DiagnosticInfo { get; set; }
  parameters: []
  return:
    type: System.String
    description: A string which represent information on the current Action.
seealso: []
---
When building an application, you may need to determine why an Action or Controller is not activated in a particular Window. This assists in finding bugs, and fixing them. For this purpose, XAF ships the [DiagnosticInfo Action](xref:112818).

To enable this Action in Windows Forms applications, set the `EnableDiagnosticActions` key in the configuration file's `appSettings` section to `True`. If you click it, a dialog window will be invoked. This window displays information on each Controller loaded to the [Application Model](xref:112580), Actions and the current Template's Action Containers.

For more information about DiagnosticInfo Action in ASP.NET Core Blazor applications, refer to the following topic: [](xref:112818).

You can supply custom diagnostic information on an Action. To do this, use the `DiagnosticInfo` property. Its value will be set for the `AdditionalInfo` item within the corresponding Controllers | Controller | Actions | Action section (see the diagnostic info snippet below).

# [XML](#tab/tabid-xml)

```XML
<Controller Name="SetPriorityController" 
            FullName="MainDemo.Module.SetPriorityController" Active="True">
  <ActiveList>
    <Item Key="View is assigned" Value="True" />
    <Item Key="Activating is allowed" Value="True" />
    <Item Key="!ViewChanging.Cancel" Value="True" />
  </ActiveList>
  <Actions>
    <Action ID="SetPriorityAction" TypeName="SingleChoiceAction" 
         Category="RecordEdit" Active="False" Enabled="True" AdditionalInfo="Hello!">
      <ActiveList>
        <Item Key="EmptyItems" Value="True" />
        <Item Key="Controller active" Value="True" />
        <Item Key="ObjectType" Value="False" />
        <Item Key="HideActionsViewController" Value="True" />
      </ActiveList>
      <EnabledList>
        <Item Key="EmptyItems" Value="True" />
        <Item Key="ByContext_RequireMultipleObjects" Value="True" />
      </EnabledList>
    </Action>
  </Actions>
</Controller>
```

***
