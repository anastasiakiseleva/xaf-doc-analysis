---
uid: "113142"
seealso:
- linkId: "113141"
title: Built-in Controllers and Actions in Extra Modules
---
# Built-in Controllers and Actions in Extra Modules

This topic lists built-in [Controllers](xref:112621) and their [Actions](xref:112622) supplied with XAF's [additional modules](xref:118046).

For more information on a particular Controller or Action, navigate to the [Application Model](xref:112580)'s  **ActionDesign** | **Controllers** or **ActionDesign** | **Actions** node in the [Model Editor](xref:112582).

To determine whether an Action is displayed in a particular window, make sure that the Template contains the Action Container that displays the Action. To determine the Action's Action Container, use the Application Model's **ActionDesign** | **ActionToContainerMapping** node.

{|
|-

! Module
! Platform-Independent
! ASP.NET Core Blazor
! Windows Forms
|-

| [Audit Trail](#audit-trail-module)
| [AuditInformationReadonlyViewController](#auditinformationreadonlyviewcontroller)

[AuditInformationListViewRefreshController](#auditinformationlistviewrefreshcontroller)

[AuditTrailListViewController](#audittraillistviewcontroller)

[AuditTrailViewController](#audittrailviewcontroller)
| &nbsp;
| &nbsp;
|-

| [Clone Object](#clone-object-module)
| [CloneObjectViewController](#cloneobjectviewcontroller)
| &nbsp;
| &nbsp;
|-

| [Conditional Appearance](#conditional-appearance-module)
| [ActionAppearanceController](#actionappearancecontroller)

[AppearanceController](#appearancecontroller)

[DetailViewItemAppearanceController](#detailviewitemappearancecontroller)

[DetailViewLayoutItemAppearanceController](#detailviewlayoutitemappearancecontroller)

[ListViewItemAppearanceController](#listviewitemappearancecontroller)

[RefreshAppearanceController](#refreshappearancecontroller)

[RefreshItemsAppearanceControllerBase\<T>](#refreshitemsappearancecontrollerbaset)
| &nbsp;
|-

| [Dashboards](#dashboards-module)
| [DashboardNavigationController](#dashboardnavigationcontroller)

[HideDetailViewActionsController](#hidedetailviewactionscontroller)

[NewDashboardController](#newdashboardcontroller)
| [BlazorDashboardNewObjectActionImageController](#blazordashboardnewobjectactionimagecontroller)

[BlazorHideDetailViewNewActionController](#blazorhidedetailviewnewactioncontroller)

[BlazorHideRefreshActionController](#blazorhiderefreshactioncontroller)

[BlazorNewDashboardController](#blazornewdashboardcontroller)

[DashboardConfirmationUnsavedChangesController](#dashboardconfirmationunsavedchangescontroller)

[ExportToXmlController](#exporttoxmlcontroller)

[WorkingModeSwitchController](#workingmodeswitchcontroller)
| [WinEditDashboardController](#wineditdashboardcontroller)

[WinExportDashboardController](#winexportdashboardcontroller)

[WinNewDashboardController](#winnewdashboardcontroller)

[WinPrintDashboardController](#winprintdashboardcontroller)

[WinShowDashboardDesignerController](#winshowdashboarddesignercontroller)
|-

| [File Attachments](#file-attachments-module)
| &nbsp;
| &nbsp;
| [FileAttachmentControllerBase](#fileattachmentcontrollerbase)

[FileAttachmentController](#fileattachmentcontroller-for-windows-forms)

[FileAttachmentListViewController](#fileattachmentlistviewcontroller)
|-

| [Office](#office-module)
| &nbsp;
| [BlazorMailMergeController](#blazormailmergecontroller)

[BlazorShowInDocumentController](#blazorshowindocumentcontroller)
| [MailMergeController](#mailmergecontroller)

[MenuManagerController](#menumanagercontroller)

[OfficeActionsController](#officeactionscontroller)

[RichTextGridController](#richtextgridcontroller)

[RichTextServiceController](#richtextservicecontroller)

[ShowDocumentInPopupController](#showdocumentinpopupcontroller)

[ShowInDocumentController](#showindocumentcontroller)

[SpreadsheetMenuManagerController](#spreadsheetmenumanagercontroller)

[SpreadsheetServiceController](#spreadsheetservicecontroller)

[SpreadsheetShowDocumentInPopupController](#spreadsheetshowdocumentinpopupcontroller)

|-

| [Reports V2](#reports-v2-module)
| [CopyPredefinedReportsController](#copypredefinedreportscontroller)

[CustomizeNavigationItemsController](#customizenavigationitemscontroller8203)

[DeleteReportController](#deletereportcontroller)

[NewReportWizardController](#newreportwizardcontroller)

[PreviewReportDialogController](#previewreportdialogcontroller)

[PrintSelectionBaseController](#printselectionbasecontroller)

[ReportsControllerCore](#reportscontrollercore)

[ReportServiceController](#reportservicecontroller)
| [BlazorReportServiceController](#blazorreportservicecontroller)

[BlazorEditReportController](#blazoreditreportcontroller)

[BlazorReportWizardDialogController](#blazorreportwizarddialogcontroller)

[HideToolbarController](#hidetoolbarcontroller)

[ReportsController](#reportscontroller)

[ReportProcessViewShortcutController](#reportprocessviewshortcutcontroller)

| [WinReportsController](#winreportscontroller)

[WinReportServiceController](#winreportservicecontroller)

|-

| [Scheduler](#scheduler-module)
| [SchedulerListViewControllerBase](#schedulerlistviewcontrollerbase)

[SchedulerRecurrenceInfoControllerBase](#schedulerrecurrenceinfocontrollerbase)

[SchedulerResourceController](#schedulerresourcecontroller)
| [DisableValidationOnListViewController](#disablevalidationonlistviewcontroller)

[EnableValidationOnDetailViewController](#enablevalidationondetailviewcontroller)

[SchedulerDataSourceFilterController](#schedulerdatasourcefiltercontroller)

[SchedulerDetailViewController](#schedulerdetailviewcontroller)

[SchedulerDisableActionsController](#schedulerdisableactionscontroller)

[SchedulerListViewController](#schedulerlistviewcontroller-for-aspnet-core-blazor)

[SchedulerOperationsSecurityController](#scheduleroperationssecuritycontroller)

[SchedulerRecurrenceInfoController](#schedulerrecurrenceinfocontroller-for-aspnet-core-blazor)
| [SchedulerModificationsController](#schedulermodificationscontroller)

[SchedulerListViewController](#schedulerlistviewcontroller-for-windows-forms)

[SchedulerRecurrenceInfoController](#schedulerrecurrenceinfocontroller-for-windows-forms)

[SchedulerResourceDeletingController](#schedulerresourcedeletingcontroller)

|-

| [Security System](#security-system)
| [ChangePasswordController](#changepasswordcontroller)

[HasRightsToModifyMemberController](#hasrightstomodifymembercontroller)

[MyDetailsController](#mydetailscontroller)

[PermissionsController](#permissionscontroller)

[RefreshSecurityController](#refreshsecuritycontroller)

[ResetPasswordController](#resetpasswordcontroller)
| &nbsp;
| &nbsp;
| &nbsp;
|-

| [State Machine](#state-machine-module)
| [DisableStatePropertyController](#disablestatepropertycontroller)

[StateMachineAppearanceController](#statemachineappearancecontroller)

[StateMachineController](#statemachinecontroller)

[StateMachineControllerBase\<T>](#statemachinecontrollerbaset)
| &nbsp;
| &nbsp;
| &nbsp;
|-

| [TreeList Editors](#treelist-editors-module)
| [TreeListEditorRootValueController](#treelisteditorrootvaluecontroller)
| &nbsp;
| [CategoryController](#categorycontroller)

[TreeListEditorColumnChooserController](#treelisteditorcolumnchoosercontroller)

[TreeNodeController](#treenodecontroller)
| &nbsp;
|-

| [Validation Module](#validation-module)
| [ActionValidationController](#actionvalidationcontroller)

[CheckContextsAvailableController](#checkcontextsavailablecontroller)

[PersistenceValidationController](#persistencevalidationcontroller)

[PreventValidationDetailsAccessController](#preventvalidationdetailsaccesscontroller)

[ResultsHighlightController](#resultshighlightcontroller)

[ShowAllContextsController](#showallcontextscontroller)

[ShowRulesController](#showrulescontroller)
| [DisableActionsController](#disableactionscontroller)

[InplaceEditorsValidationControllerBlazor](#inplaceeditorsvalidationcontrollerblazor)

[ValidationController](#validationcontroller)
| [ContextValidationResultController](#contextvalidationresultcontroller)

[CustomizeErrorMessageColumnController](#customizeerrormessagecolumncontroller)

[SuppressToolBar](#suppresstoolbar)

[ValidationResultsShowingController](#validationresultsshowingcontroller)
| &nbsp;
|-

| [View Variants Module](#view-variants-module)
| [ChangeVariantController](#changevariantcontroller)

[CustomizeNavigationItemsController](#customizenavigationitemscontroller82038203)
| &nbsp;
| &nbsp;
| &nbsp;
|}

## Audit Trail Module

### Platform-Independent

#### AuditInformationReadonlyViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.AuditTrail.Xpo.v<:xx.x:>.dll_.

Actions: none.

Activated for Views that display `IBaseAuditDataItemPersistent` objects. Makes these Views read-only to prohibit users from editing audit information.

***

#### AuditInformationListViewRefreshController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.AuditTrail.Xpo.v<:xx.x:>.dll_.

Actions: none.

Activated for nested List Views that display `IBaseAuditDataItemPersistent` objects. Makes new audit entries accessible after the corresponding changes to object are saved.

***

#### AuditTrailListViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.AuditTrail.Xpo.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Used internally. When XAF loads a collection with a criterion, the Controller changes the audit type to `ObjectChanged` (if the `ObjectLoaded` type was set previously).

***

#### AuditTrailViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.AuditTrail.Xpo.v<:xx.x:>.dll_.

Actions: none.

Activated for root Detail Views. Activates the system of auditing changes for the XPO session in which a View is invoked.

***

## Clone Object Module

### Platform-Independent

#### CloneObjectViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.CloneObject.v<:xx.x:>.dll_.

Actions: none.

Activated for List and Detail Views. Contains the **Clone** Action. This Action allows users to clone an object selected in a List View or the current object in a Detail View. It invokes a Detail View with a new object and copies the property values from the original object.

**See Also:** [](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController)

***

## Conditional Appearance Module

### Platform-Independent

#### ActionAppearanceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ConditionalAppearance.v<:xx.x:>.dll_.

Actions: none.

Activated for List and Detail Views. Collects Actions mentioned in the current object's appearance rules and refreshes their appearance.

***

#### AppearanceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ConditionalAppearance.v<:xx.x:>.dll_.

Actions: none.

Activated for List and Detail Views. Collects the current appearance rules declared for the business object (see [](xref:DevExpress.ExpressApp.ConditionalAppearance.IModelConditionalAppearance) and [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute)). Exposes the `RefreshItemAppearance` method used by other module controllers to refresh the appearance.

**See Also:** [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceController)

***

#### DetailViewItemAppearanceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ConditionalAppearance.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Refreshes Detail View items' appearance.

***

#### DetailViewLayoutItemAppearanceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ConditionalAppearance.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Refreshes layout items' appearance.

***

#### ListViewItemAppearanceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ConditionalAppearance.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Refreshes the current [](xref:DevExpress.ExpressApp.Editors.ListEditor) appearance if the editor supports the `ISupportAppearanceCustomization` interface.

***

#### RefreshAppearanceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ConditionalAppearance.v<:xx.x:>.dll_.

Actions: none.

Activated for List and Detail Views. Refreshes the appearance when the [View.SelectionChanged](xref:DevExpress.ExpressApp.View.SelectionChanged), [View.CurrentObjectChanged](xref:DevExpress.ExpressApp.View.CurrentObjectChanged), [BaseObjectSpace.ObjectChanged](xref:DevExpress.ExpressApp.BaseObjectSpace.ObjectChanged), and [BaseObjectSpace.Committed](xref:DevExpress.ExpressApp.BaseObjectSpace.Committed) events occur.

***

#### RefreshItemsAppearanceControllerBase\<T>

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ConditionalAppearance.v<:xx.x:>.dll_.

Actions: none.

The [DetailViewItemAppearanceController](#detailviewitemappearancecontroller)'s and [DetailViewLayoutItemAppearanceController](#detailviewlayoutitemappearancecontroller)'s abstract base class.

***

## Dashboards Module

### Platform-Independent

#### DashboardNavigationController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Dashboards.v<:xx.x:>.dll_.

Actions: none.

Assigns a [](xref:DevExpress.ExpressApp.ViewShortcut) to Dashboard Detail View for each navigation item that supports the [](xref:DevExpress.ExpressApp.Dashboards.IModelDashboardNavigationItem) interface.

***

### HideDetailViewActionsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Dashboards.v<:xx.x:>.dll_.

Actions: none.

Activated for the "DashboardViewer_DetailView" Detail View. Deactivates the [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController), [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController) and [](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController) to prohibit the creation, editing, and deletion of dashboard instances.

***

### NewDashboardController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Dashboards.v<:xx.x:>.dll_.

Actions: none

The [WinNewDashboardController](#winnewdashboardcontroller)'s base class. Implements the common functionality required to create new Dashboards.

***

### ASP.NET Core Blazor

#### BlazorDashboardNewObjectActionImageController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Dashboards.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Views that display @DevExpress.Persistent.Base.IDashboardData objects. Updates @DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction's `ImageName` to the dashboard-specific image.

***

#### BlazorHideDetailViewNewActionController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Dashboards.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views that display @DevExpress.Persistent.Base.IDashboardData objects. Deactivates the [NewObjectViewController](xref:113141#newobjectviewcontroller).

***

#### BlazorHideRefreshActionController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Dashboards.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views that display @DevExpress.Persistent.Base.IDashboardData objects. Deactivates the [RefreshController](xref:113141#refreshcontroller).

***

#### BlazorNewDashboardController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Dashboards.Blazor.v<:xx.x:>.dll_.

Actions: none.

A [NewDashboardController](#newdashboardcontroller) descendant. Contains Blazor-specific code that allows users to create new dashboards.

***

#### DashboardConfirmationUnsavedChangesController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Dashboards.Blazor.v<:xx.x:>.dll_.

Actions: none.

Implements "unsaved changes" confirmation dialog functionality in @DevExpress.ExpressApp.Dashboards.Blazor.Components.BlazorDashboardViewerViewItem.

***

#### ExportToXmlController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Dashboards.Blazor.v<:xx.x:>.dll_.

Actions: **DashboardExportToXml**.

Activated for Detail Views that display @DevExpress.Persistent.Base.IDashboardData objects. Exports dashboard content to XML.

***

#### WorkingModeSwitchController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Dashboards.Blazor.v<:xx.x:>.dll_.

Actions: **DashboardSwitchToDesigner**, **DashboardSwitchToViewer**.

Activated for Detail Views that display @DevExpress.Persistent.Base.IDashboardData objects. Includes Actions that change [DxDashboard.WorkingMode](xref:DevExpress.DashboardBlazor.DxDashboard.WorkingMode).

***

### Windows Forms

#### WinEditDashboardController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Dashboards.Win.v<:xx.x:>.dll_.

Actions: **ShowDesignerAction**.

Activated in [](xref:DevExpress.Persistent.Base.IDashboardData) objects' List and Detail Views. The **ShowDesignerAction** Action allows users to modify dashboards in the Dashboard Designer. Uses [WinShowDashboardDesignerController](#winshowdashboarddesignercontroller) to show the [WinForms Dashboard Designer](xref:117006).

***

#### WinExportDashboardController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Dashboards.Win.v<:xx.x:>.dll_.

Actions: **ExportAction**.

Activated for the "DashboardViewer_DetailView" Detail View. The **ExportAction** Action allows users to export the dashboards to various formats.

***

### WinNewDashboardController

Platform: Windows Forms. Assembly: _DevExpress.ExpressApp.Dashboards.Win.v<:xx.x:>.dll_.

Inherits the [NewDashboardController](#newdashboardcontroller). Contains Windows Forms specific code to create new dashboards. Uses [WinShowDashboardDesignerController](#winshowdashboarddesignercontroller) to show the [WinForms Dashboard Designer](xref:117006).

***

#### WinPrintDashboardController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Dashboards.Win.v<:xx.x:>.dll_.

Actions: **PrintAction**.

Activated for the "DashboardViewer_DetailView" Detail View. The **PrintAction** Action allows users to print the current dashboard.

***

#### WinShowDashboardDesignerController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Dashboards.Win.v<:xx.x:>.dll_.

Actions: none.

Contains the [](xref:DevExpress.ExpressApp.Dashboards.Win.DashboardDesignerManager) instance. Exposes the `ShowDesigner` and the `GetDashboardData` methods the Dashboards Module Controllers use to show the [WinForms Dashboard Designer](xref:117006) and then get the modified [](xref:DevExpress.Persistent.Base.IDashboardData) object.

***

## File Attachments Module

### Windows Forms

#### FileAttachmentControllerBase

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.FileAttachment.Win.v<:xx.x:>.dll_.

Actions: **Open**, **SaveTo**.

The base class that implements the [FileAttachmentController](#fileattachmentcontroller-for-windows-forms)'s and [FileAttachmentListViewController](#fileattachmentlistviewcontroller)'s common functionality.

***

#### FileAttachmentController for Windows Forms

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.FileAttachment.Win.v<:xx.x:>.dll_.

Actions: **Open**, **SaveTo**.

Activated when the current View's object type uses the `FileAttachment` attribute. The **Open** Action allows users to open a file using an associated application. The **Save** Action allows users to save a file to a local disk.

**See Also:**[](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentController)

***

#### FileAttachmentListViewController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.FileAttachment.Win.v<:xx.x:>.dll_.

Actions: **AddFromFile**.

Activated for List Views where the object type uses the `FileAttachment` attribute. Contains the **AddFromFile** Action that allows users to add file attachments to List Views using a standard Open File dialog. This Controller also supports drag-and-drop functionality to add file attachments to a List View.

**See Also:**[](xref:DevExpress.ExpressApp.FileAttachments.Win.FileAttachmentListViewController)

***

## Office Module

### ASP.NET Core Blazor

#### BlazorMailMergeController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Office.Blazor.v<:xx.x:>.dll_.

Actions: none.

A `RichTextMailMergeControllerBase` descendant. Activated for Detail Views that display `IRichTextMailMergeData` objects. Contains Blazor-specific code that supports the [Mail Merge](xref:400006) feature.

***

#### BlazorShowInDocumentController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Office.Blazor.v<:xx.x:>.dll_.

Actions: **ShowInDocument**.

A `RichTextShowInDocumentControllerBase` descendant. The **ShowInDocument** Action is activated for Views where the object type is used in Mail Merge Template objects.

***

### Windows Forms

#### MailMergeController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.
 
Activated for Views that display `IRichTextMailMergeData` objects. Implements the common [Mail Merge](xref:400006) functionality. Allows you to customize Mail Merge settings.

***

#### MenuManagerController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for Views that contain `RichTextPropertyEditor`. Creates a Menu Manager for the `RichTextPropertyEditor`, depending on the application settings (see [Use Rich Text Documents in Business Objects](xref:400004)). Allows you to customize ribbon menu and bars.

***

#### OfficeActionsController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: **OpenAction**, **SaveAsAction**

Activated for Views that contain `RichTextPropertyEditor` or `SpreadsheetPropertyEditor`. Customizes print actions for the main menu and application button. The **OpenAction** allows users to open a document in different formats. The **SaveAsAction** allows users to save document to the file system in different formats.

***

#### RichTextGridController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Applies internal settings to `RichEditControl` before `GridView` displays it in a cell. Allows you to customize the control.

***

#### RichTextServiceController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.

Allows you to customize the `RichEditControl` and `RichTextRibbonForm`.

***

#### ShowDocumentInPopupController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for Views that contain `RichTextPropertyEditor`. Adds a context menu item. This item opens the content of the current rich text editor in a pop-up window. Allows you to customize `RichTextRibbonForm`.

***

#### ShowInDocumentController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: **ShowInDocument**

Activated for Views. The **ShowInDocument** Action is activated for Views where the object type is used in Mail Merge Template objects. 

***

#### SpreadsheetMenuManagerController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for Views that contain `SpreadsheetPropertyEditor`. Creates a Menu Manager for the `SpreadsheetPropertyEditor`, depending on the application settings . For more information, refer to the following topic: [Use Spreadsheet Documents in Business Objects](xref:400931). Allows you to customize ribbon menu and bars.

***

#### SpreadsheetServiceController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.

Allows you to customize `SpreadsheetControl` and its `RibbonControl`.

***

#### SpreadsheetShowDocumentInPopupController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Office.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for Views that contain `SpreadsheetPropertyEditor`. Adds a context menu item. This item opens the content of the current Spreadsheet editor in a pop-up window. Allows you to customize `SpreadsheetRibbonForm`.

***

## Reports V2 Module

### Platform-Independent

#### CopyPredefinedReportsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: **CopyPredefinedReport**.

Activated in List Views that display [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) objects. Provides the **CopyPredefinedReport** Action used to copy a selected predefined read-only report to an editable report.

***

#### CustomizeNavigationItemsController&#8203;

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: none.

Activated in the main window. Adds the contextual Reports navigation groups. These groups expose navigation items providing users with instant access to reports related to a certain navigation item when TreeList navigation is enabled.

***

#### DeleteReportController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: none.

Activated in List Views that display [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) objects. Disables the **Delete** action in the [](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController) when the selected objects contain a predefined report.

***

#### NewReportWizardController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: none.

Activated in List Views that display [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) objects. Allows users to create new reports using a report wizard.

***

#### PreviewReportDialogController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: **Accept**, **Cancel**.

A [](xref:DevExpress.ExpressApp.SystemModule.DialogController) descendant activated for the report parameters dialog. Introduces custom **Accept** and **Cancel** actions.

**See Also:**[](xref:DevExpress.ExpressApp.ReportsV2.PreviewReportDialogController)

***

#### PrintSelectionBaseController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: **ShowInReport**.

Activated in all Views. Provides the **ShowInReport** used to execute [In-Place Reports](xref:113602).

**See Also:**[](xref:DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController) | [PrintSelectionBaseController.ShowInReportAction](xref:DevExpress.ExpressApp.ReportsV2.PrintSelectionBaseController.ShowInReportAction)

***

### ReportsControllerCore

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: **ExecuteReport**.

Activated in List Views that display [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) objects. Provides the **ExecuteReport** Action used to execute a selected report.

**See Also:**[](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController) | [ReportsControllerCore.ExecuteReportAction](xref:DevExpress.ExpressApp.ReportsV2.ReportsControllerCore.ExecuteReportAction)

***

#### ReportServiceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ReportsV2.v<:xx.x:>.dll_.

Actions: none.

Contains the common code used to display the Preview Report window. Exposes the [ReportServiceController.ShowPreview](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController.ShowPreview*) method that invokes the Preview Report window.

**See Also:**[](xref:DevExpress.ExpressApp.ReportsV2.ReportServiceController)

***

### ASP.NET Core Blazor

#### BlazorReportServiceController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.ReportsV2.Blazor.v<:xx.x:>.dll_.

Actions: none.

A [ReportServiceController](#reportservicecontroller) descendant. Contains platform-specific code that displays the Preview Report window in XAF ASP.NET Core Blazor applications.

***

#### BlazorEditReportController

Actions: **EditReportAction**.

An `EditReportControllerCore` descendant. Activated in List Views that display @DevExpress.ExpressApp.ReportsV2.IReportDataV2 objects. Contains platform-specific code that allows users to edit a report in XAF ASP.NET Core Blazor applications.

***

#### BlazorReportWizardDialogController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.ReportsV2.Blazor.v<:xx.x:>.dll_.

Actions: **ReportWizard_Create**, **ReportWizard_Close**.

A @DevExpress.ExpressApp.SystemModule.DialogController descendant. A report-specific controller with custom **Accept** and **Cancel** Actions.

***

#### HideToolbarController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.ReportsV2.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Report Detail Views. Hides the main toolbar.

***

#### ReportsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.ReportsV2.Blazor.v<:xx.x:>.dll_.

Actions: **ExecuteReport**.

A [ReportsControllerCore](#reportscontrollercore) descendant. Activated in List Views that display @DevExpress.ExpressApp.ReportsV2.IReportDataV2 objects. Implements the **ExecuteReport** Action.

***

### ReportProcessViewShortcutController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.ReportsV2.Blazor.v<:xx.x:>.dll_.

Actions: none.

Handles the `ProcessViewShortcutController.CustomProcessShortcut` event to manage [View Shortcuts](xref:DevExpress.ExpressApp.ViewShortcut) related to Report Views.

***

### Windows Forms

### WinReportsController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.ReportsV2.Win.v<:xx.x:>.dll_.

Actions: none.

Inherits the [ReportsControllerCore](#reportscontrollercore) Controller. Activated in List Views that display [](xref:DevExpress.ExpressApp.ReportsV2.IReportDataV2) objects. Initializes the [ReportsControllerCore.ExecuteReportAction](xref:DevExpress.ExpressApp.ReportsV2.ReportsControllerCore.ExecuteReportAction) Action.

**See Also:** [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportsController)

***

#### WinReportServiceController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.ReportsV2.Win.v<:xx.x:>.dll_.

Actions: none.

The controller is inherited from the [ReportServiceController](#reportservicecontroller). Contains Windows Forms-specific code that allows users to create, design, and view reports.

**See Also:** [](xref:DevExpress.ExpressApp.ReportsV2.Win.WinReportServiceController)

***

## Scheduler Module

### Platform-Independent

#### SchedulerChangedOccurrencesController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Scheduler.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views that display `IEvent` objects.

Designed to create Exceptions for [Recurring Events](xref:113128) when they are changed.

***

#### SchedulerListViewControllerBase

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Scheduler.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views that display `IEvent` objects. This is a base Controller for the platform-specific `SchedulerListViewControllers`.

***

#### SchedulerRecurrenceInfoControllerBase

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Scheduler.v<:xx.x:>.dll_.

Actions: none.

Activated in Detail Views of the objects that implement the `IRecurrentEvent` interface. It is a base class for Windows Forms `SchedulerRecurrenceInfo` Controllers. Manages the Property Editor of the `Recurrence` property.

***

#### SchedulerResourceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Scheduler.v<:xx.x:>.dll_. Actions: none.

Activated in Detail Views that display the objects that implement the `IRecurrentEvent` interface.

Make the resources collection read-only when the current Detail View visualizes an occurrence. A resources collection can be edited for the entire series only.

***

### ASP.NET Core Blazor

#### DisableValidationOnListViewController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views that display `IEvent` objects. Disables validation for Warning and Information rules (@DevExpress.ExpressApp.Validation.ValidationModule.IgnoreWarningAndInformationRules set to `true`).

***

#### EnableValidationOnDetailViewController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views that display `IEvent` objects. Enables validation for Warning and Information rules (@DevExpress.ExpressApp.Validation.ValidationModule.IgnoreWarningAndInformationRules set to `false`).

***

#### SchedulerDataSourceFilterController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Filters @DevExpress.Blazor.DxScheduler's Data Source by the current date interval.

***

#### SchedulerDetailViewController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Refreshes the @DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor when an Appointment Edit Form is closed.

***

#### SchedulerDisableActionsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Deactivates the [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) if the List View uses a @DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor.

***

#### SchedulerListViewController for ASP.NET Core Blazor

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

A [SchedulerListViewControllerBase](#schedulerlistviewcontrollerbase) descendant. Contains platform-specific code that allows the @DevExpress.Blazor.DxScheduler control to work in an XAF application.

***

#### SchedulerNestedResourcesVisibilityController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for nested List Views. Sets [DxScheduler.VisibleResourcesDataSource](xref:DevExpress.Blazor.DxScheduler.VisibleResourcesDataSource) based on the master object.

***

#### SchedulerOperationsSecurityController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Adjusts @DevExpress.Blazor.DxScheduler settings to prevent data change that are prohibited by the security system.

***

#### SchedulerRecurrenceInfoController for ASP.NET Core Blazor

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Scheduler.Blazor.v<:xx.x:>.dll_.

Actions: none.

A [SchedulerRecurrenceInfoControllerBase](#schedulerrecurrenceinfocontrollerbase) descendant. Contains Blazor-specific code that manages the Property Editor of the `Recurrence` property.

***

### Windows Forms

#### SchedulerListViewController for Windows Forms

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Scheduler.Win.v<:xx.x:>.dll_.

Actions: none.

The controller is inherited from the [SchedulerListViewControllerBase](#schedulerlistviewcontrollerbase) Controller. Contains Windows Forms-specific code that sets up the `Scheduler` control to work in an XAF application.

***

#### SchedulerModificationsController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Scheduler.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views that display `IEvent` objects. For internal use. When a Detail View is invoked from the List View displayed by @DevExpress.ExpressApp.Scheduler.Blazor.Editors.SchedulerListEditor, this Controller refreshes the Scheduler editor when an object is changed or a change is committed in the Detail View.

***

#### SchedulerRecurrenceInfoController for Windows Forms

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Scheduler.Win.v<:xx.x:>.dll_.

Actions: none.

The controller is inherited from the [SchedulerRecurrenceInfoControllerBase](#schedulerrecurrenceinfocontrollerbase) Controller. Contains Windows Forms specific code to manage the Property Editor of the `Recurrence` property.

***

#### SchedulerResourceDeletingController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Scheduler.Win.v<:xx.x:>.dll_. Actions: none.

Activated for Detail Views displaying `IResource` objects. Displays the "Please refresh the event detail view to load changes" warning when the current object is deleted. The message is [localizable](xref:112595) under the **Localization** | **Messages** | **SchedulerResourceDeletingWarning** node.

***

## Security System

### Platform-Independent

#### ChangePasswordController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Security.v<:xx.x:>.dll_.

Actions: **ChangePasswordByUser**.

Activated for the **My Details** Detail View. The **ChangePasswordByUser** Action allows users to change their password. The `ChangePasswordController` class calls the [IAuthenticationStandardUser.SetPassword](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser.SetPassword(System.String)) method to change the password and modify the selected object. The **ChangePasswordByUser** action is available when a user selects an object that is the [SecuritySystem.CurrentUser](xref:DevExpress.ExpressApp.SecuritySystem.CurrentUser) entry and its [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property is updated dynamically when the selected object is changed.

**See Also:** [Passwords in the Security System](xref:112649) | [SecurityModule.TryUpdateLogonParameters](xref:DevExpress.ExpressApp.Security.SecurityModule.TryUpdateLogonParameters(System.String,System.Object)) | [PermissionPolicyUser.SetPassword](xref:DevExpress.Persistent.BaseImpl.PermissionPolicy.PermissionPolicyUser.SetPassword(System.String)) | [PermissionPolicyUser.SetPassword](xref:DevExpress.Persistent.BaseImpl.EF.PermissionPolicy.PermissionPolicyUser.SetPassword(System.String))

***

#### HasRightsToModifyMemberController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Security.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Makes Property Editors read-only or editable depending on the current user's rights to edit the current object. When a Property Editor displays a property of an object set to a reference property, this Controller sets it as read-only or editable, depending on the rights to edit the referenced object.

**See Also:** [](xref:DevExpress.ExpressApp.Security.HasRightsToModifyMemberController)

***

#### MyDetailsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Security.v<:xx.x:>.dll_.

Actions: **MyDetails**.

Activated in the main window. Adds the **My Details** item to the navigation control. When a user clicks this item, a Detail View with the current User's details is displayed. This Action shows a Detail View with the current user's details.

**See Also:** [](xref:DevExpress.ExpressApp.Security.MyDetailsController)

***

#### PermissionsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Security.v<:xx.x:>.dll_.

Actions: none.

Activated for Views where object type implements the `IPersistentPermission` interface. Manages the creation of new permissions. Replaces the **New** Action's predefined types with the found types inherited from the `PermissionBase` class. The Detail View invoked when using the **New** Action displays a new `PermissionBase` object where the **Permission** property references the permission selected in the **New** Action's `Items` collection.

***

#### RefreshSecurityController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Security.v<:xx.x:>.dll_.

Actions: none.

Activated for root List and Detail Views displaying User objects. Refreshes the permission set when the current user object is changed.

***

#### ResetPasswordController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Security.v<:xx.x:>.dll_.

Actions: **ResetPasswordAction**.

Activated for root Views. Designed for a security system that uses the authentication strategy implementing the `IAuthenticationStandard` interface, and the **User** type implementing the [](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser) interface. Contains the **ResetPasswordAction** Action. This Action allows users that possess "Write" access to the User type to set a new password for users. Internally the Action calls the [IAuthenticationStandardUser.SetPassword](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser.SetPassword(System.String)) method and modifies the [IAuthenticationStandardUser.ChangePasswordOnFirstLogon](xref:DevExpress.Persistent.Base.Security.IAuthenticationStandardUser.ChangePasswordOnFirstLogon) property. When the selected user object is changed, `ResetPasswordController` checks that the current user is permitted to modify the `StoredPassword` and `ChangePasswordOnFirstLogon` properties of the selected object and updates the **ResetPassword** action's [ActionBase.Enabled](xref:DevExpress.ExpressApp.Actions.ActionBase.Enabled) property. The names of these properties are not obtained dynamically. Instead, these strings are specified by the `PasswordFieldName` and `ChangePasswordOnFirstLogonFieldName` properties, which are declared as static.

**See Also:** [Passwords in the Security System](xref:112649)

***

## State Machine Module

### Platform-Independent

#### DisableStatePropertyController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.StateMachine.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Prohibits editing of the state property by setting its Property Editor's `AllowEdit` property to `false`.

**See Also:** [PropertyEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit)

***

#### StateMachineAppearanceController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.StateMachine.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views and Detail Views. Collects conditional appearance rules declared in state machines associated with currently displayed objects and adds these rules to the list of currently active conditional appearance rules.

**See Also:** [State Machine Module](xref:113336) | [Conditional Appearance Module Overview](xref:113286)

***

#### StateMachineController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.StateMachine.v<:xx.x:>.dll_.

Actions: **ChangeState**.

Activated for List Views and Detail Views. Displays the **ChangeState** [Action](xref:112622) for objects that have associated state machines. The Action allows users to change object states via a UI.

**See Also:** [State Machine Module](xref:113336)

***

#### StateMachineControllerBase\<T>

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.StateMachine.v<:xx.x:>.dll_.

Actions: none.

A generic abstract base class from which State Machine module Controllers are derived. Contains basic functionality, such as retrieving state machines associated with the object the current [View](xref:112611) displays.

**See Also:** [View.CurrentObject](xref:DevExpress.ExpressApp.View.CurrentObject)

***

## TreeList Editors Module

### Platform-Independent

#### TreeListEditorColumnChooserController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.TreeListEditors.Win.v<:xx.x:>.dll_.

Actions: none.

The controller is inherited from the [System Module](xref:113141)'s `ColumnChooserControllerBase` Controller. Sets up the Tree List Editor's Customization form and supports its functionality. This form can be invoked by selecting a Column Chooser in the grid's context menu.

***

#### TreeListEditorRootValueController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.TreeListEditors.v<:xx.x:>.dll_.

Actions: none.

Activated for nested List Views. Allows the Child collection of an [](xref:DevExpress.Persistent.Base.General.ITreeNode) object to be displayed via the TreeList control in the object's Detail View.

***

### Windows Forms

#### CategoryController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.TreeListEditors.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for all Views. Works with business classes that implement the [](xref:DevExpress.Persistent.Base.General.ICategorizedItem) interface. This Controller automatically sets a category for newly created objects.

***

#### TreeNodeController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.TreeListEditors.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for root Views. Works with business classes that implement the [](xref:DevExpress.Persistent.Base.General.ITreeNode) interface. This Controller links a newly created object to its parent.

***

## Validation Module

### Platform-Independent

#### ActionValidationController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_.

Actions: none.

Extends the Application Model' [](xref:DevExpress.ExpressApp.Model.IModelAction) node with the [IModelActionValidationContexts.ValidationContexts](xref:DevExpress.ExpressApp.Validation.IModelActionValidationContexts.ValidationContexts) property. Subscribes to the `Executing` event of all Actions available in the current [](xref:DevExpress.ExpressApp.Frame). In the event handler, checks validation rules associated with the context that is set for the Action's **ValidationContexts** property. If at least one rule is broken, it cancels the Action's execution and raises a validation exception.

***

#### CheckContextsAvailableController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_.

Actions: none.

Activated in all windows. Deactivates the [ShowAllContextsController](#showallcontextscontroller)'s **ShowAllContexts** Action, if no validation rules are specified for the current View's object type.

***

#### PersistenceValidationController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_.

Actions: none.

Subscribes to the [BaseObjectSpace.ObjectDeleting](xref:DevExpress.ExpressApp.BaseObjectSpace.ObjectDeleting) and [BaseObjectSpace.Committing](xref:DevExpress.ExpressApp.BaseObjectSpace.Committing) events. In the event handlers, checks validation rules associated with the [DefaultContexts.Save](xref:DevExpress.Persistent.Validation.DefaultContexts.Save) and [DefaultContexts.Delete](xref:DevExpress.Persistent.Validation.DefaultContexts.Delete) validation contexts. If at least one rule is broken, it cancels execution of the Save/Delete operation and raises a validation exception.

**See Also:** [](xref:DevExpress.ExpressApp.Validation.PersistenceValidationController)

***

#### PreventValidationDetailsAccessController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views displaying the `DisplayableValidationResultItem` objects. Prevents invoking the `DisplayableValidationResultItem` Detail View via the **ListViewShowObject** Action (see [ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction)) when the `ValidationModule.AllowValidationAccess` property is set to `false`.

***

#### ResultsHighlightController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_.

Actions: none.

Activated for all Views. When validation rules are broken, this controller adds messages to the [View.ErrorMessages](xref:DevExpress.ExpressApp.View.ErrorMessages) collection. This results in displaying error images near Property Editors with invalid data.

**See Also:** [GitHub Example: XAF - How to Highlight Invalid Properties Immediately in an Invoked View](https://github.com/DevExpress-Examples/xaf-how-to-highlight-invalid-properties-when-a-view-is-activated)

***

#### ShowAllContextsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_.

Actions: **ShowAllContexts**.

Activated for all Views. The **ShowAllContexts** Action checks all rules designed for the current View's object type. In a List View, selected objects are checked. In a Detail View, the current object is checked. The result appears in a separate window where all checked rules are grouped by context.

***

#### ShowRulesController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.Validation.v<:xx.x:>.dll_.

Actions: none.

Activated in all windows. The `DiagnosticInfoProviderBase` descendant. Provides the information on rules that are currently available in the Application Model for `DiagnosticInfoController`. `DiagnosticInfoController` adds the **Rules Info** Single Choice Action Item **DiagnosticInfo** Action. When a user selects this item, the collected information is shown in an invoked window.

**See Also:** [Determine Why an Action, Controller or Editor is Inactive](xref:112818)

***

### ASP.NET Core Blazor

#### DisableActionsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Validation.Blazor.v<:xx.x:>.dll_.

Actions: none.

Deactivates the [ShowAllContextsController](#showallcontextscontroller).

***

#### InplaceEditorsValidationControllerBlazor

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Validation.Blazor.v<:xx.x:>.dll_.

Actions: none.

An `InplaceEditorsValidationControllerBase` descendant. Contains Blazor-specific code that handles the [PropertyEditor.ValueStored](xref:DevExpress.ExpressApp.Editors.PropertyEditor.ValueStored) event to validate an in-place editor's value.

***

#### ValidationController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Validation.Blazor.v<:xx.x:>.dll_.

Actions: none.

Contains Blazor-specific code that deals with validation alert manipulation.

***

### Windows Forms

#### ContextValidationResultController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Validation.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views displaying `ContextValidationResult` objects. Customizes the [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) settings, so the height of each row is automatically adjusted to display its cells' contents.

***

#### CustomizeErrorMessageColumnController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Validation.Win.v<:xx.x:>.dll_.

Actions: none.

This Controller uses the [GridListEditor.GridView](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor.GridView) and `XafGridView.ErrorMessages` properties to show Error/Warning/Info icon in the **Description** column of the "RuleSetValidationResultItem_ByTarget_ListView" List View (see [Declare Validation Rules](xref:113251)). This Controller is not designed to work with other List Editors. Deactivate it if you need to use another List Editor class to show objects in the 'RuleSetValidationResultItem_ByTarget_ListView' list view.

***

#### SuppressToolBar

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Validation.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for nested List Views of Detail Views displayed when a validation rule is broken, or the **ShowAllContexts** Action is executed. Hides the List View's toolbar using the `ToolbarVisibilityController`'s methods.

***

#### ValidationResultsShowingController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Validation.Win.v<:xx.x:>.dll_.

Actions: none.

Activated in the main Window. When a validation exception occurs, it shows a validation error Detail View in the exception error window.

***

## View Variants Module

### Platform-Independent

#### ChangeVariantController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ViewVariantsModule.v<:xx.x:>.dll_.

Actions: **ChangeVariant**.

Activated for all Views. The **ChangeVariant** Action allows users to switch between predefined View variants of a particular business object type. Its items are specified by the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariants) node of the Application Model.

**See Also:** [](xref:DevExpress.ExpressApp.ViewVariantsModule.ChangeVariantController)

***

#### CustomizeNavigationItemsController&#8203;&#8203;

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.ViewVariantsModule.v<:xx.x:>.dll_.

Actions: none.

Activated in the main Window. Adds the contextual View Variants navigation groups. These groups expose navigation items, providing users with instant access to View Variants related to a certain navigation item when TreeList navigation is enabled. Extends the Application Model with the [](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelNavigationItemsVariantSettings) interface.

***