## Windows Forms

You can use the following values with the `Shortcut` property:

* A [System.Windows.Forms.Shortcut](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.shortcut) enumeration value in string format (for example, `CtrlShiftO`).
* A [System.Windows.Forms.Keys](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.keys) enumeration value in string format (for example, `LShiftKey`).
* Several [System.Windows.Forms.Keys](https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.keys) values in string format separated by "+" (for example, `Control+Shift+O`).

The following table contains default shortcuts you can use to execute Actions in XAF Windows Forms applications:

| Action | Shortcut |
|---|---|
| NavigateBack | Alt+LeftArrow |
| NavigateForward | Alt+RightArrow|
| New | Ctrl+N |
| Save | Ctrl+S |
| Delete | Ctrl+D |
| SaveAndClose | Control+Enter |
| Refresh | F5 |
| EditModel | Ctrl+Shift+F1 |
| Print (from the [Printing Module](xref:113012)) | Ctrl+P |
| Open (from the FileAttachments module) | Ctrl+O |
| SaveTo (from the FileAttachments module) | Ctrl+Shift+S |

> [!NOTE]
> XAF Windows Forms applications do not support multiple shortcuts for a single Action.