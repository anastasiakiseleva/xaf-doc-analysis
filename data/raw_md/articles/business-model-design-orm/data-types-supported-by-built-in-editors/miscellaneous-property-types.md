---
uid: "113576"
seealso:
- linkId: "113366"
- linkId: "402188"
title: Miscellaneous Property Types
owner: Anastasiya Kisialeva
---
# Miscellaneous Property Types

This topic describes Property Editors shipped with XAF's built-in modules.

## ASP.NET Core Blazor Property Editors

[!include[blazor-editor-descendants](~/templates/blazor-editor-descendants.md)]

### RichTextPropertyEditor

![|XAF ASP.NET Core Blazor RichTextPropertyEditor, DevExpress|](~/images/xaf-blazor-richtextpropertyeditor-devexpress.png)

Data type: `byte[]` or `String`

Component: @DevExpress.Blazor.RichEdit.DxRichEdit

Namespace: `DevExpress.ExpressApp.Office.Blazor.Editors`

`RichTextPropertyEditor` ships with the [Office Module](xref:400003). You can use it in List and Detail Views. Use `RichTextPropertyEditor` to [edit rich text documents](xref:400004) and create [Mail Merge](xref:400006) templates. For more information about this Property Editor, refer to the following topic: [](xref:400004).

### SchedulerLabelPropertyEditor

![XAF ASP.NET Core Blazor SchedulerLabelPropertyEditor, DevExpress](~/images/xaf-blazor-schedulerlabelpropertyeditor-devexpress.png)

Data type: `IEvent.Label`

Component: @DevExpress.Blazor.DxComboBox`2

Namespace: @DevExpress.ExpressApp.Scheduler.Blazor.Editors

`SchedulerLabelPropertyEditor` displays the `Label` property of a business class that implements the built-in `DevExpress.Persistent.Base.General.IEvent` interface. For more information about Scheduler-specific properties and Property Editors, refer to the following topic: [](xref:112812#properties-and-corresponding-property-editors).

`SchedulerLabelPropertyEditor` ships with the [Scheduler Module](xref:112811). Its control is an image combo box. Items in the combo box are @DevExpress.Blazor.DxSchedulerAppointmentLabelItem objects.

For information on how to customize the `Label` property, refer to the following topic: [](xref:404714).

### SchedulerStatusPropertyEditor

![XAF ASP.NET Core Blazor SchedulerStatusPropertyEditor, DevExpress](~/images/xaf-blazor-schedulerstatuspropertyeditor-devexpress.png)

Data type: `IEvent.Status`

Component: @DevExpress.Blazor.DxComboBox`2

Namespace: [DevExpress.ExpressApp.Scheduler.Blazor.Editors](xref:DevExpress.ExpressApp.Scheduler.Blazor.Editors)

`SchedulerStatusPropertyEditor` displays the `Status` property of a business class that implements the built-in `DevExpress.Persistent.Base.General.IEvent` interface. For more information about Scheduler-specific properties and Property Editors, refer to the following topic: [](xref:112812#properties-and-corresponding-property-editors).

 `SchedulerStatusPropertyEditor` ships with the [Scheduler Module](xref:112811). Its control is an image combo box populated by @DevExpress.Blazor.DxSchedulerAppointmentStatusItem objects.

For information on how to customize the `Status` property, refer to the following topic: [](xref:404714).

### SchedulerRecurrenceInfoPropertyEditor

![XAF ASP.NET Core Blazor SchedulerRecurrenceInfoPropertyEditor, DevExpress](~/images/xaf-blazor-schedulerrecurrencepropertyeditor-1-devexpress.png)

![XAF ASP.NET Core Blazor Pop-up SchedulerRecurrenceInfoPropertyEditor, DevExpress](~/images/xaf-blazor-schedulerrecurrencepropertyeditor-2-devexpress.png)

Data type: `IRecurrentEvent.RecurrenceInfoXml`

Component: @DevExpress.Blazor.DxComboBox`2

Namespace: [DevExpress.ExpressApp.Scheduler.Blazor.Editors](xref:DevExpress.ExpressApp.Scheduler.Blazor.Editors)

`SchedulerRecurrenceInfoPropertyEditor` displays the `RecurrenceInfoXml` property of a business class that implements the built-in `IRecurrentEvent` interface. For more information about recurrent events in Scheduler, refer to the following topic: [](xref:113128).

`SchedulerRecurrenceInfoPropertyEditor` ships with the [Scheduler Module](xref:112811). Select a value in the drop-down list of this Property Editor to invoke a form where you can specify the current event's recurrence options.

### DefaultPropertyEditor

![|XAF ASP.NET Core Blazor DefaultPropertyEditor, DevExpress|](~/images/xaf-blazor-defaultpropertyeditor-devexpress.png)

[!include[<`DefaultPropertyEditor`>](~/templates/default-property-editor-warning.md)]

Data type: Any data type

Component: @DevExpress.Blazor.DxTextBox

Namespace: [DevExpress.ExpressApp.Blazor.Editors](xref:DevExpress.ExpressApp.Blazor.Editors)

Used as a default editor for unsupported data types. Displays the property's value in read-only mode.

### ProtectedContentPropertyEditor

![|XAF ASP.NET Core Blazor ProtectedContentPropertyEditor, DevExpress|](~/images/xaf-blazor-protectedcontentpropertyeditor-devexpress.png)

Data type: Any data type.

Namespace: [DevExpress.ExpressApp.Blazor.Editors](xref:DevExpress.ExpressApp.Blazor.Editors)

`ProtectedContentPropertyEditor` displays properties that the current user has no permission to view. This Property Editor is always read-only.

To specify custom text instead of the protected data, use the [IModelApplication.ProtectedContentText](xref:DevExpress.ExpressApp.Model.IModelApplication.ProtectedContentText) property of the [Application Model](xref:112580)'s Application node. 

[!include[security-demo-link](~/templates/security-demo-link.md)]

## Windows Forms Property Editors

[!include[PE_IntroWin](~/templates/pe_introwin111103.md)]

### RichTextPropertyEditor

![RichTextPropertyEditor-misc](~/images/RichTextPropertyEditor-misc.png)

Data type: `byte[]`

Control: `RichEditorContainer` wrapper for the @DevExpress.XtraRichEdit.RichEditControl, part of the DevExpress WinForms Subscription.

Repository Item: @DevExpress.XtraEditors.Repository.RepositoryItemRichTextEdit.

[!include[RichTextPropertyEditors-forByteArrayProperties](~/templates/RichTextPropertyEditors-forByteArrayProperties.md)] `RichTextPropertyEditor`.

### SpreadsheetPropertyEditor

![SpreadsheetPropertyEditor-misc](~/images/SpreadsheetPropertyEditor-misc.png)

Data type: `byte[]`

Control: `SpreadsheetContainer` wrapper for @DevExpress.XtraSpreadsheet.SpreadsheetControl, part of the DevExpress WinForms Subscription.

Repository Item: No repository item available. You cannot use this Property Editor in List Views.

`SpreadsheetPropertyEditor` ships with the [Office Module](xref:400003). Use this Property Editor to edit [spreadsheet documents](xref:400931).

### ChartPropertyEditor

![ChartPropertyEditor](~/images/chartpropertyeditor116816.png)

Data type: `IChartDataSourceProvider`

Control: [](xref:DevExpress.XtraCharts.ChartControl)

Repository Item: No repository item available. List Views display a textual representation of an `IChartDataSourceProvider` object.

### SchedulerLabelPropertyEditor

![SchedulerLabelPropertyEditor_Transparent](~/images/schedulerlabelpropertyeditor_transparent115877.png)

Data type: `IEvent.Label`

Control: [](xref:DevExpress.XtraScheduler.UI.AppointmentLabelEdit) editor, part of the DevExpress WinForms Subscription.

Repository Item: No repository item available. The Scheduler control displays the `Event.Label` property in a custom manner.

`SchedulerLabelPropertyEditor` displays the `Label` property of a business class that implements the built-in `DevExpress.Persistent.Base.General.IEvent` interface. For more information about Scheduler-specific properties and Property Editors, refer to the following topic: [](xref:112812#properties-and-corresponding-property-editors).

`SchedulerLabelPropertyEditor` ships with the [Scheduler Module](xref:112811). Its control is an image combo box populated by the [](xref:DevExpress.XtraScheduler.AppointmentLabel) objects. These objects are stored in the control's [](xref:DevExpress.XtraScheduler.SchedulerStorage). To access them, use the [AppointmentStorage.Labels](xref:DevExpress.XtraScheduler.AppointmentStorage.Labels) collection returned by the [SchedulerStorage.Appointments](xref:DevExpress.XtraScheduler.SchedulerStorage.Appointments) property.

To expand the editor's drop-down window, use Alt + Down Arrow.

### SchedulerStatusPropertyEditor

![SchedulerStatusPropertyEditor_Transparent](~/images/schedulerstatuspropertyeditor_transparent115879.png)

Data type: `IEvent.Status`

Control: [](xref:DevExpress.XtraScheduler.UI.AppointmentStatusEdit) editor, part of the DevExpress WinForms Subscription.

Repository Item: No repository item available. The Scheduler control displays the `Event.Label` property in a custom manner.

`SchedulerStatusPropertyEditor` displays the `Status` property of a business class that implements the built-in `DevExpress.Persistent.Base.General.IEvent` interface. For more information about Scheduler-specific properties and Property Editors, refer to the following topic: [](xref:112812#properties-and-corresponding-property-editors).

`SchedulerStatusPropertyEditor` ships with the [Scheduler Module](xref:112811). Its control is an image combo box populated by the [](xref:DevExpress.XtraScheduler.AppointmentStatus) objects. These objects are contained in the control's [](xref:DevExpress.XtraScheduler.SchedulerStorage). To access them, use the [AppointmentStorage.Statuses](xref:DevExpress.XtraScheduler.AppointmentStorage.Statuses) collection returned by the [SchedulerStorage.Appointments](xref:DevExpress.XtraScheduler.SchedulerStorage.Appointments) property.

### SchedulerRecurrenceInfoPropertyEditor

![SchedulerRecurrenceInfoPropertyEditor](~/images/schedulerrecurrenceinfopropertyeditor116308.png)

Data type: `SupportRecurrences.RecurrenceInfoXml`

Control: [](xref:DevExpress.XtraEditors.ButtonEdit) editor, part of the DevExpress WinForms Subscription.

Repository Item: No repository item available. The Scheduler control displays the `IRecurrentEvent.RecurrenceInfoXml` property in a custom manner.

`SchedulerRecurrenceInfoPropertyEditor` displays the `RecurrenceInfoXml` property of a business class that implements the built-in `IRecurrentEvent` interface. For more information about recurring events in Scheduler, refer to the following topic: [](xref:113128).

`SchedulerRecurrenceInfoPropertyEditor` ships with the [Scheduler Module](xref:112811). Click or double-click the editor's ellipsis button to invoke a form where you can specify the current event's recurrence options or cancel recurrence.

### RichTextPropertyEditor

![RichTextBoxWithBinding_Transparent](~/images/richtextboxwithbinding_transparent115854.png)

Data type: `String`

Control: `RichTextBoxWithBinding` that is a descendant of the `System.Windows.Forms.RichTextBox` editor.

Repository Item: `RepositoryItemRtfEditEx` that is a descendant of the [](xref:DevExpress.XtraEditors.Repository.RepositoryItemBlobBaseEdit) repository item.

To use `RichTextPropertyEditor`, specify it in the `PropertyEditorType` property of the required **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** or [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node.

The control's height is a product of the `RowCount` property value and default row height. If the value of the `RowCount` property is not specified, it is set to 10. If it is set to 0, the application assumes that 15 rows fit in the control.

The `RepositoryItemRtfEditEx` repository item is displayed by the `RtfEditEx` editor that is the descendant of the `BlobBaseEdit` editor. This editor displays the `PopupRtfEditExForm` form as a pop-up form.

### DefaultPropertyEditor

![DefaultPropertyEditor_Collection_Transparent](~/images/defaultpropertyeditor_collection_transparent115867.png)

![DefaultPropertyEditor_SingleValue_Transparecy](~/images/defaultpropertyeditor_singlevalue_transparecy115865.png)

Data type: Any data type.

Control: [](xref:DevExpress.XtraGrid.GridControl) or `StringEdit` used by the `StringPropertyEditor`.

Repository Item: No repository item available.

[!include[<`DefaultPropertyEditor`>](~/templates/default-property-editor-warning.md)]

`DefaultPropertyEditor` is used when there is no default Property Editor for the current property's data type and the `PropertyEditorType` property of the corresponding [](xref:DevExpress.ExpressApp.Model.IModelMember) node is not specified.

`GridControl` displays data if the property type is `IEnumerable` or `ITypedList`.

`StringEdit` is used for all other property types. It displays the property value's textual representation.

Both `GridControl` and `StringEdit` display data in read-only mode by default.

### ProtectedContentPropertyEditor

![ProtectedContentEdit](~/images/protectedcontentedit115861.png)

Data type: Any data type.

Control: `ProtectedContentEdit`

Repository Item: `RepositoryItemProtectedContentTextEdit` that is a descendant of the [](xref:DevExpress.XtraEditors.Repository.RepositoryItemTextEdit) repository item.

`ProtectedContentPropertyEditor` displays properties that the current user has no permission to view. This Property Editor is always read-only.

To specify custom text instead of the protected data, use the [IModelApplication.ProtectedContentText](xref:DevExpress.ExpressApp.Model.IModelApplication.ProtectedContentText) property of the [Application Model](xref:112580)'s **Application** node.

[!include[security-demo-link](~/templates/security-demo-link.md)]
