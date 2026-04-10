---
uid: "113141"
seealso:
- linkId: "113142"
title: Built-in Controllers and Actions in the System Module
---
# Built-in Controllers and Actions in the System Module

This topic lists built-in [Controllers](xref:112621) and their [Actions](xref:112622) supplied with System's base, ASP.NET Core Blazor, and Windows Forms modules.

For more information on individual Controllers or Actions, navigate to the [Application Model](xref:112580)'s  **ActionDesign** | **Controllers** or **ActionDesign** | **Actions** node in the [Model Editor](xref:112582).

**[CRUD](#create-read-update-and-delete-crud)**
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[CheckDeletedObjectController](#checkdeletedobjectcontroller)<br/>[DeleteObjectsViewController](#deleteobjectsviewcontroller)<br/>[DependentEditorController](#dependenteditorcontroller)<br/>[LinkDialogController](#linkdialogcontroller)<br/>[LinkNewObjectController](#linknewobjectcontroller)<br/>[LinkToListViewController](#linktolistviewcontroller)<br/>[LinkUnlinkController](#linkunlinkcontroller)<br/>[ModificationsController](#modificationscontroller)<br/>[NewObjectViewController](#newobjectviewcontroller) | [BlazorModificationsController](#blazormodificationscontroller)<br/>[BlazorNewObjectViewController](#blazornewobjectviewcontroller) | [WinModificationsController](#winmodificationscontroller)<br/>[WinNewObjectViewController](#winnewobjectviewcontroller)
**[Search and Filtering](#search-and-filtering)**
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[FilterController](#filtercontroller)<br/>[FindLookupDialogController](#findlookupdialogcontroller)<br/>[FindLookupNewObjectDialogController](#findlookupnewobjectdialogcontroller) | [LookupSearchDialogController](#lookupsearchdialogcontroller)<br/>[LookupSearchNewObjectController](#lookupsearchnewobjectcontroller) | |

**[Navigation](#navigation)**
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[RecordsNavigationController](#recordsnavigationcontroller)<br/>[ShowNavigationItemController](#shownavigationitemcontroller)<br/>[ViewNavigationController](#viewnavigationcontroller) | [BlazorRecordsNavigationController](#blazorrecordsnavigationcontroller)<br/>[BlazorViewNavigationController](#blazorviewnavigationcontroller)<br/>[NavigationSettingsController](#navigationsettingscontroller)<br/>[ProcessViewShortcutController](#processviewshortcutcontroller) | [WinShowStartupNavigationItemController](#winshowstartupnavigationitemcontroller)<br/>[WinViewNavigationController](#winviewnavigationcontroller)

**[List Views](#list-views)**
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[AutoFilterRowListViewController](#autofilterrowlistviewcontroller)<br/>[ListEditorPreviewRowViewController](#listeditorpreviewrowviewcontroller)<br/>[ListViewProcessCurrentObjectController](#listviewprocesscurrentobjectcontroller)<br/>[NewItemRowListViewController](#newitemrowlistviewcontroller) | [BlazorExportController](#blazorexportcontroller)<br/>[ColumnChooserController](#columnchoosercontroller)<br/>[DxGridListEditorColumnContextMenuController](#dxgridlisteditorcolumncontextmenucontroller)<br/>[DxGridListEditorPreviewRowController](#dxgridlisteditorpreviewrowcontroller)<br/>[FilterEditorController](#filtereditorcontroller)<br/>[GridBatchModificationsDisplayController](#gridbatchmodificationsdisplaycontroller)<br/>[GridEditingRefreshController](#grideditingrefreshcontroller)<br/>[ListViewContextMenuActionsController](#listviewcontextmenuactionscontroller)<br/>[ListEditorInplaceEditController](#listeditorinplaceeditcontroller) | [ColumnChooserControllerBase](#columnchoosercontrollerbase)<br/>[GridEditorColumnChooserController](#grideditorcolumnchoosercontroller)<br/>[GridListEditorController](#gridlisteditorcontroller)<br/>[GridListEditorPreviewRowController](#gridlisteditorpreviewrowcontroller)<br/>[ListEditorNewObjectController](#listeditornewobjectcontroller)<br/>[ListViewFocusedElementToClipboardController](#listviewfocusedelementtoclipboardcontroller)<br/>[NewItemRowDataSourcePropertyController](#newitemrowdatasourcepropertycontroller)<br/>[ToolbarVisibilityController](#toolbarvisibilitycontroller)

[Security](#security)
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[LogoffController](#logoffcontroller)<br/>[LogonController](#logoncontroller) | [BlazorLogonController](#blazorlogoncontroller) | |

[Dashboards](#dashboards)
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[DashboardCreationWizardController](#dashboardcreationwizardcontroller)<br/>[DashboardCustomizationController](#dashboardcustomizationcontroller)<br/>[DashboardDeactivateItemsActionsController](#dashboarddeactivateitemsactionscontroller)<br/>[DashboardOrganizerHideToolbarController](#dashboardorganizerhidetoolbarcontroller)<br/>[DashboardOrganizerItemsCollectionsController](#dashboardorganizeritemscollectionscontroller)<br/>[DeleteDashboardsController](#deletedashboardscontroller)<br/>[ViewDashboardOrganizationItemController](#viewdashboardorganizationitemcontroller) | &nbsp; | [DashboardWinLayoutManagerController](#dashboardwinlayoutmanagercontroller)

[Debugging and Testing](#debugging-and-testing)
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[DiagnosticInfoProviderBase](#diagnosticinfoproviderbase)<br/>[DiagnosticInfoController](#diagnosticinfocontroller)<br/>[ViewInfoController](#viewinfocontroller) | [EasyTestAssistanceController](#easytestassistancecontroller) | [LookupControlFinderController](#lookupcontrolfindercontroller)<br/>[WindowControlFinderController](#windowcontrolfindercontroller)

[Miscellaneous](#miscellaneous)
:   Platform-Independent | ASP.NET Core Blazor |Windows Forms
---------|----------|---------
[ActionsCriteriaViewController](#actionscriteriaviewcontroller)<br/>[DetailViewEditorActionController](#detailvieweditoractioncontroller)<br/>[DetailViewLinkController](#detailviewlinkcontroller)<br/>[DialogController](#dialogcontroller)<br/>[ExportController](#exportcontroller)<br/>[FillActionContainersController](#fillactioncontainerscontroller)<br/>[FocusDefaultDetailViewItemController](#focusdefaultdetailviewitemcontroller)<br/>[HideActionsViewController](#hideactionsviewcontroller)<br/>[ObjectMethodActionsViewController](#objectmethodactionsviewcontroller)<br/>[RefreshController](#refreshcontroller)<br/>[ResetViewSettingsController](#resetviewsettingscontroller)<br/>[WindowTemplateController](#windowtemplatecontroller) | [ActionHandleExceptionController](#actionhandleexceptioncontroller)<br/>[BlazorResetViewSettingsController](#blazorresetviewsettingscontroller)<br/>[BlazorRibbonController](#blazorribboncontroller)<br/>[CloseDetailViewController](#closedetailviewcontroller)<br/>[ConfirmationActionRegistrationController](#confirmationactionregistrationcontroller)<br/>[ConfirmationDetailViewController](#confirmationdetailviewcontroller)<br/>[ConfirmationListViewController](#confirmationlistviewcontroller)<br/>[ConfirmationUnsavedLinkedObjectController](#confirmationunsavedlinkedobjectcontroller)<br/>[CustomizeActionControlController](#customizeactioncontrolcontroller)<br/>[CustomizeBlazorActionContainerViewItemController](#customizeblazoractioncontainerviewitemcontroller)<br/>[DetailViewRefreshController](#detailviewrefreshcontroller)<br/>[DisableDashboardLayoutEditorController](#disabledashboardlayouteditorcontroller)<br/>[DisableLayoutEditorController](#disablelayouteditorcontroller)<br/>[DisableNestedLayoutEditorController](#disablenestedlayouteditorcontroller)<br/>[LayoutEditorConfirmationController](#layouteditorconfirmationcontroller)<br/>[ManageActionVisibilityController](#manageactionvisibilitycontroller)<br/>[ObjectModelController](#objectmodelcontroller)<br/>[PopupWindowTemplateClosingController](#popupwindowtemplateclosingcontroller)<br/>[PopupWindowTemplateSizeController](#popupwindowtemplatesizecontroller)<br/>[PrimaryToolbarItemsController](#primarytoolbaritemscontroller) | [AboutInfoController](#aboutinfocontroller)<br/>[AboutInfoFormController](#aboutinfoformcontroller)<br/>[AsyncLoadingCancelationController](#asyncloadingcancelationcontroller)<br/>[AsyncLoadingIndicationController](#asyncloadingindicationcontroller)<br/>[ChooseSkinController](#chooseskincontroller)<br/>[ConfigureSkinController](#configureskincontroller)<br/>[CloseMdiChildWindowController](#closemdichildwindowcontroller)<br/>[CloseWindowController](#closewindowcontroller)<br/>[DockPanelsVisibilityController](#dockpanelsvisibilitycontroller)<br/>[EditModelController](#editmodelcontroller)<br/>[ExitController](#exitcontroller)<br/>[HtmlFormattingController](#htmlformattingcontroller)<br/>[LockController](#lockcontroller)<br/>[MdiTabImageController](#mditabimagecontroller)<br/>[OpenObjectController](#openobjectcontroller)<br/>[PrintingController](#printingcontroller)<br/>[VersionsCompatibilityController](#versionscompatibilitycontroller)<br/>[WaitCursorController](#waitcursorcontroller)<br/>[WinExportController](#winexportcontroller)<br/>[WinFocusDefaultDetailViewItemController](#winfocusdefaultdetailviewitemcontroller)<br/>[WinFocusListEditorControlController](#winfocuslisteditorcontrolcontroller)<br/>[WinLayoutManagerController](#winlayoutmanagercontroller)<br/>[WinWindowTemplateController](#winwindowtemplatecontroller)<br/>[XtraGridInLookupController](#xtragridinlookupcontroller)

> [!NOTE]
> In this topic, we refer to built-in Actions using their [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id) property values. Use the Model Editor to find out which caption is assigned to an Action.

## Create, Read, Update and Delete (CRUD)

### Platform-independent

#### CheckDeletedObjectController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views.

Makes the current Detail View read-only and displays the "Data is displayed in read-only mode, because it has been deleted." message if the View's object has been deleted.

***

#### DeleteObjectsViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **Delete**.

Activated for all Views. Contains the **Delete** Action. This Action allows users to delete the current object displayed in a Detail View or the currently selected object(s) in a List View. Note that objects deleted from nested collections are not deleted at once. They are deleted when a user saves the entire root object.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController) | [DeleteObjectsViewController.DeleteAction](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.DeleteAction) | [DeleteObjectsViewController.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.DeleteObjectsViewController.AutoCommit)

***

#### DependentEditorController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Updates fields that display the values of an object's reference properties when a reference property is changed.

***

#### LinkDialogController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

A [DialogController](#dialogcontroller) descendant. Activated in the **Link** Action's pop-up window if it supports the [Search functionality](xref:112925). Adds the [LinkNewObjectController](#linknewobjectcontroller) to the window, invoked when pressing the **New** button. Executes the **FullTextSearch** Action to retrieve the newly created object to the current List View's collection.

**See Also:** [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) | [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) | [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925)

***

#### LinkNewObjectController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

A [DialogController](#dialogcontroller) descendant. Activated in the pop-up window that is invoked when the **New** button is pressed in the **Link** Action's pop-up window. When the **OK** button is pressed, this Controller saves the newly created object, and passes it to the [LinkDialogController](#linkdialogcontroller), so that it can be selected in the **Link** Action's pop-up window.

**See Also:** [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) | [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925)

***

#### LinkToListViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

For internal use. Creates a **Link** object used by the [DetailViewLinkController](#detailviewlinkcontroller) to synchronize changes made in a Detail View invoked from the List View.

***

#### LinkUnlinkController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **Link**, **Unlink**.

Activated for nested List Views. The **Link** Action allows users to add an existing object to the current nested collection. The objects to be chosen are displayed by a List View in a pop-up window. The **Unlink** Action deletes references to the object selected in the current nested collection. The changes made to a collection are not saved immediately; they are saved when the root object is saved.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController) | [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) | [LinkUnlinkController.UnlinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.UnlinkAction) | [LinkUnlinkController.AutoCommit](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.AutoCommit)

***

#### ModificationsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **Cancel**, **Save**, **SaveAndClose**, **SaveAndNew**.

Activated for Detail Views. Creates and manages the active and enabled state of the **Cancel**, **Save**, **SaveAndClose**, and **SaveAndNew** Actions.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.ModificationsController) | [ModificationsController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.CancelAction) | [ModificationsController.SaveAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAction) | [ModificationsController.SaveAndCloseAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndCloseAction) | [ModificationsController.SaveAndNewAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndNewAction) | [ModificationsController.ModificationsCheckingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsCheckingMode) | [ModificationsController.ModificationsHandlingMode](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.ModificationsHandlingMode)

***

#### NewObjectViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **New**.

Activated for all Views. The **New** Action allows users to create a new object of the type selected from the list of predefined types. To specify predefined types in the Model Editor, add child nodes to the **CreatableItems** node. To specify a predefined type in code, use the `NavigationItem` attribute, or handle the Controller's `CollectCreatableItemTypes` and `CollectDescendantTypes` events.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController) | [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) | [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems) | [](xref:DevExpress.Persistent.Base.NavigationItemAttribute) | [NewObjectViewController.CollectDescendantTypes](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.CollectDescendantTypes) | [How to: Customize the New Action's Items List](xref:112915)

***

### ASP.NET Core Blazor

#### BlazorModificationsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: inherited.

A [ModificationsController](#modificationscontroller) descendant activated for Object Views.

***

#### BlazorNewObjectViewController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: inherited.

A [NewObjectViewController](#newobjectviewcontroller) descendant activated for Object Views. Overrides the `UpdateActionsState` method to populate the [`NewObjectViewController.NewObjectAction`](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection with objects of the current View's object type (including descendants).

***

### Windows Forms

#### WinModificationsController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: inherited.

A [ModificationsController](#modificationscontroller)'s descendant. Activated for Object Views.

**See Also:** [](xref:DevExpress.ExpressApp.Win.SystemModule.WinModificationsController)

***

#### WinNewObjectViewController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: inherited.

The controller is inherited from the [NewObjectViewController](#newobjectviewcontroller). Overrides the **UpdateActionsState** method to populate the **New** Action's [ChoiceActionBase.Items](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase.Items) collection. The current View's object type, its descendants, and the types listed in the Application Model's **CreatableItems** node are added to the collection.

**See Also:** [](xref:DevExpress.ExpressApp.Win.SystemModule.WinNewObjectViewController) | [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction) | [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems)

***

## Search and Filtering

### Platform-independent

#### FilterController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **SetFilter**, **FullTextSearch**.

Activated for List Views. The **SetFilter** Action allows users to select one of the predefined filters created for the current List View. The **FullTextSearch** Action allows users to search objects that match the entered text. In addition to Actions, this Controller filters the current List View's data source according to the criteria specified in the Application Model.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.FilterController) | [FilterController.SetFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.SetFilterAction) | [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) | [Filters Application Model Node](xref:112992) | [FullTextSearch Action](xref:112997) | [Criteria Property in the Application Model](xref:112990)

***

#### FindLookupDialogController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

A [DialogController](#dialogcontroller)'s descendant. Activated in the Lookup Property Editor's lookup window if the search functionality is enabled.

Adds the [FindLookupNewObjectDialogController](#findlookupnewobjectdialogcontroller) to the invoked window when pressing the **New** button. Executes the **FullTextSearch** Action to select the newly created object in the current List View's collection.

**See Also:** [IModelOptions.LookupSmallCollectionItemCount](xref:DevExpress.ExpressApp.Model.IModelOptions.LookupSmallCollectionItemCount) | [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925)

***

#### FindLookupNewObjectDialogController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

A [DialogController](#dialogcontroller)'s descendant. Activated in the pop-up window that is invoked when pressing the **New** button in a Lookup Property Editor's lookup window. When the **OK** button is pressed, this Controller saves the newly created object and passes it to the [FindLookupDialogController](#findlookupdialogcontroller), so that it can be selected in the Lookup Property Editor's lookup window.

***

### ASP.NET Core Blazor

#### LookupSearchDialogController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: **EditRowAction**.

A [DialogController](#dialogcontroller) descendant. If [Search functionality](xref:112925#search-functionality) is enabled for a [LookupPropertyEditor](xref:113572), this controller activates in the **Search** Action's pop-up window. Adds a [LookupSearchNewObjectController](#lookupsearchnewobjectcontroller) to all windows created with the **New** or **Clone** buttons.

**See Also:** [LookupPropertyEditor](xref:113572) | [FilterController.FullTextFilterAction](xref:DevExpress.ExpressApp.SystemModule.FilterController.FullTextFilterAction) | [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925)

#### LookupSearchNewObjectController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: **EditRowAction**.

A [DialogController](#dialogcontroller) descendant. Activated in the pop-up window that is invoked when you click the **New** or **Clone** button in the **Search** Action's pop-up window of [LookupPropertyEditor](xref:113572). When you click the **OK** button, the Controller saves the created object and passes it to the editor's property value.

**See Also:** [LookupPropertyEditor](xref:113572) | [How to: Add a Search Action to Lookup Property Editors and Link Pop-up Windows](xref:112925)

## Navigation

### Platform-independent

#### RecordsNavigationController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **PreviousObject**, **NextObject**.

Activated for all Views. The **PreviousObject** Action is intended to navigate to the previous object in the collection source. When using this Action for a List View, the previous object in the View's editor is selected. When using this Action in a Detail View that displays an object currently selected in a List View, the previous object in the List View's editor is shown in the Detail View. The **NextObject** Action does the same, but navigates to the next object in the collection.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController) | [RecordsNavigationController.PreviousObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.PreviousObjectAction) | [RecordsNavigationController.NextObjectAction](xref:DevExpress.ExpressApp.SystemModule.RecordsNavigationController.NextObjectAction)

***

#### ShowNavigationItemController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **ShowNavigationItem**.

Activated in the main window. The **ShowNavigationItem** Action allows users to navigate between predefined Views. In a Windows Forms application, this Action is displayed by the navigation bar. The Views to which you can navigate using this Action are specified in the Application Model's [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController) | [ShowNavigationItemController.ShowNavigationItemAction](xref:DevExpress.ExpressApp.SystemModule.ShowNavigationItemController.ShowNavigationItemAction) | [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItems) | [Navigation System](xref:113198)

***

#### ViewNavigationController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **NavigateBack**, **NavigateForward**.

Activated in all windows. The Actions implemented by this controller allow users to navigate to recently invoked Views. These Actions are activated in the main window only.

***

### ASP.NET Core Blazor

#### BlazorRecordsNavigationController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: inherited.

A [RecordsNavigationController](#recordsnavigationcontroller) descendant that activates **Next Object** and **Previous Object** Actions in a List View with a Split Layout. For more information about the Split Layout, refer to the following topic: [MasterDetailMode.ListViewAndDetailView](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailMode).

***

#### BlazorViewNavigationController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: inherited.

A [ViewNavigationController](#viewnavigationcontroller) descendant that implements Blazor-specific functionality for the **NavigateBackAction**.

***

#### NavigationSettingsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Supplies [IModelApplicationNavigationItems.NavigationItems](xref:DevExpress.ExpressApp.SystemModule.IModelApplicationNavigationItems.NavigationItems) to the `ShowNavigationItemActionControl`.

#### ProcessViewShortcutController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Handles a [View Shortcut](xref:DevExpress.ExpressApp.ViewShortcut) obtained from the current page URL.

***

### Windows Forms

#### WinShowStartupNavigationItemController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated in the main window. Displays a View when the start-up window is shown. Uses the [ShowNavigationItemController](#shownavigationitemcontroller) to get a start-up navigation item and execute the **ShowNavigationItem** Action.

***

#### WinViewNavigationController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: inherited.

The Windows Forms-specific version of the [ViewNavigationController](#viewnavigationcontroller).

***

## List Views

### Platform-independent

#### AutoFilterRowListViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views.

Extends the Application Model's [](xref:DevExpress.ExpressApp.Model.IModelClass) interface with the [](xref:DevExpress.ExpressApp.SystemModule.IModelClassShowAutoFilterRow) interface and the [](xref:DevExpress.ExpressApp.Model.IModelListView) interface with the [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewShowAutoFilterRow) interface.

**See Also:** [Application Model Basics](xref:112580) | [Application Model Structure](xref:112580) | [Extend and Customize the Application Model in Code](xref:112810)

***

#### ListEditorNewObjectController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Manages creation of new objects using [List Editors](xref:113189) by handling the [ListEditor.NewObjectAdding](xref:DevExpress.ExpressApp.Editors.ListEditor.NewObjectAdding), [ListEditor.NewObjectCreated](xref:DevExpress.ExpressApp.Editors.ListEditor.NewObjectCreated), and [ListEditor.NewObjectCanceled](xref:DevExpress.ExpressApp.Editors.ListEditor.NewObjectCanceled) events.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController)

***

#### ListEditorPreviewRowViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Extends the [Application Model](xref:112580) with the `PreviewColumnName` property of the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node. Serves as the base class for Controllers that activate preview rows in platform-specific List Editors. There are three platform-specific descendants: `DxGridListEditorPreviewRowController`, [GridListEditorPreviewRowController](#gridlisteditorpreviewrowcontroller).

**See Also:** [IModelListViewPreviewColumn.PreviewColumnName](xref:DevExpress.ExpressApp.SystemModule.IModelListViewPreviewColumn.PreviewColumnName) | [](xref:DevExpress.ExpressApp.Model.IModelListView)

***

#### ListViewProcessCurrentObjectController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **ListViewShowObject**.

Activated for List Views. The **ListViewShowObject** Action is executed when you double-click an object in a List View in a Windows Forms application. The object is displayed in a separate Window. If you need to execute a custom Action instead of the **ListViewShowObject** Action, deactivate this Controller and subscribe to the [ListView.ProcessSelectedItem](xref:DevExpress.ExpressApp.ListView.ProcessSelectedItem) event in a custom Controller.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController) | [ListViewProcessCurrentObjectController.ProcessCurrentObjectAction](xref:DevExpress.ExpressApp.SystemModule.ListViewProcessCurrentObjectController.ProcessCurrentObjectAction) | [How to: Replace a List View's Default Action](xref:112820)

***

#### NewItemRowListViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Extends the [Application Model](xref:112580) with the `DefaultListViewNewItemRowPosition` property in the **BOModel** | **_\<Class\>_** node and the `NewItemRowPosition` property in the [!include[Node_Views_ListView](~/templates/node_views_listview111381.md)] node. Configures the new item row, if the List Editor implements the [](xref:DevExpress.ExpressApp.ISupportNewItemRowPosition) interface.

**See Also:** [IModelClassNewItemRow.DefaultListViewNewItemRowPosition](xref:DevExpress.ExpressApp.SystemModule.IModelClassNewItemRow.DefaultListViewNewItemRowPosition) | [IModelListViewNewItemRow.NewItemRowPosition](xref:DevExpress.ExpressApp.SystemModule.IModelListViewNewItemRow.NewItemRowPosition)

***

### ASP.NET Core Blazor

#### BlazorExportController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: inherited.

An [ExportController](#exportcontroller) descendant. The **Export to** Action exports List View data to a memory stream. This Action is only displayed in List Views whose @DevExpress.ExpressApp.Model.IModelListView.EditorType is @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor. XAF uses the data-aware export that ships with the DevExpress Blazor Grid. For more information about this functionality and its limitations, refer to the following topics: [](xref:404338) and [](xref:113362).

***

#### ColumnChooserController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: **ColumnChooser**.

Implements a Column Chooser with the help of the @DevExpress.Blazor.DxGrid.ShowColumnChooser(DevExpress.Blazor.DialogDisplayOptions) method. The **ColumnChooser** Action is active if the current List View uses a @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor and the [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) property is set to `true`.

***

#### DxGridListEditorColumnContextMenuController

Platform: ASP.NET Core Blazor

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Implements a context menu for grid column headers. Menu actions allow users to shape grid data (filter/search, sort, group) or customize the layout (show or hide columns). To disable this menu, deactivate the controller:

```csharp
using DevExpress.ExpressApp.Blazor.SystemModule;
using DevExpress.ExpressApp;

namespace SolutionName.Blazor.Server.Controllers;

public class RemoveContextMenuController : Controller {
    protected override void OnActivated() {
        base.OnActivated();
        if (Frame.GetController<DxGridListEditorColumnContextMenuController>() is { Active: { } active1 }) {
            active1["DisableReason"] = false;
        }
    }
}
```

***

#### DxGridListEditorPreviewRowController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

A [ListEditorPreviewRowViewController](#listeditorpreviewrowviewcontroller) descendant activated in List Views. Initializes the preview section if the List View uses a @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor.

**See also:** @DevExpress.ExpressApp.SystemModule.IModelListViewPreviewColumn.PreviewColumnName

***

#### FilterEditorController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: **FilterEditorAction**.

Displays a **FilterEditorAction** if the List View uses a @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor. This Action creates a pop-up Detail View with a [FilterPropertyEditor](xref:113564#filterpropertyeditor).

***

#### GridBatchModificationsDisplayController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Tracks changes made to the Object Space for ListView in Batch mode. Customizes grid appearance to display values that are modified and not yet committed.

***

#### GridEditingRefreshController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Refreshes  @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor's property editors in certain circumstances when the grid is in [editing](xref:DevExpress.Blazor.DxGrid.IsEditing) mode.

***

#### ListViewContextMenuActionsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Implements a context menu that can be invoked for grid rows. Menu actions allow users to work with individual objects (create, clone, delete, or export). To disable this menu, deactivate the controller:

```csharp
using DevExpress.ExpressApp.Blazor.SystemModule;
using DevExpress.ExpressApp;

namespace SolutionName.Blazor.Server.Controllers;

public class RemoveContextMenuController : Controller {
    protected override void OnActivated() {
        base.OnActivated();
        if (Frame.GetController<ListViewContextMenuActionsController>() is { Active: { } active1 }) {
            active1["DisableReason"] = false;
        }
    }
}
```

***

#### ListEditorInplaceEditController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Override its `AutoCommitChanges` property to commit changes automatically in a nested List View. For more information, refer to the following topic: [](xref:113249#commit-changes-automatically-in-nested-views).

***

### Windows Forms

#### ColumnChooserControllerBase

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

The base Controller for the [GridEditorColumnChooserController](#grideditorcolumnchoosercontroller) and [WinLayoutManagerController](#winlayoutmanagercontroller). 
Adds the **Add** and **Remove** buttons to a grid's Column Chooser or Field List. When pressing the **Add** button, the Controller shows a tree representing current object properties.

***

#### GridEditorColumnChooserController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

A [ColumnChooserControllerBase](#columnchoosercontrollerbase) descendant. Intended for List Views that are displayed with the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor), which uses the **XtraGrid** editor. The Controller sets up the editor's **Customization** form and supports its functionality. This form can be invoked by selecting the **Column Chooser** in the grid's context menu.

***

#### GridListEditorController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Sets up the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) if it displays the current List View. Intended for internal use.

***

#### GridListEditorPreviewRowController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. A [ListEditorPreviewRowViewController](#listeditorpreviewrowviewcontroller) descendant. 
Initializes the preview section, if the List View uses the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor).

***

#### ListViewFocusedElementToClipboardController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **CopyCellValue**.

Activated for List Views. The **CopyCellValue** Action, implemented by this Controller, allows you to copy the contents of the focused List Editor cell to the clipboard. The List Editor should support the [](xref:DevExpress.ExpressApp.Win.Editors.IFocusedElementCaptionProvider) interface.

***

#### NewItemRowDataSourcePropertyController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. For internal use. Allows users to use the lookup editors in the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor)'s New Item Row.

***

#### ToolbarVisibilityController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **ToggleToolbarVisibility**.

Activated for nested List Views. The **ToggleToolbarVisibility** Action allows users to hide the toolbar that accompanies a nested List View. This Action can be accessed by right-clicking a nested List View, and selecting **Toggle Toolbar** in the invoked context menu.

***

## Security

### Platform-independent

#### LogoffController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **LogOff**.

Activated for all Views. The **LogOff** Action allows users to log on to the application using another user account. This Action is available when the Standard Authentication strategy is used and is deactivated when the Active Directory Authentication strategy is used.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.LogoffController) | [LogoffController.LogoffAction](xref:DevExpress.ExpressApp.SystemModule.LogoffController.LogoffAction) | [Security System](xref:113366)

***

#### LogonController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: inherited.

A [DialogController](#dialogcontroller) descendant. Activated in the Logon window. Replaces the **DialogController**'s **DialogOk** Action with the **Logon** Action. The Action's **Execute** event handler is provided by the base **DialogController** class.

**See Also:** [Security System](xref:113366)

***

### ASP.NET Core Blazor

#### BlazorLogonController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: inherited.

A [LogonController](#logoncontroller) descendant. Deactivates the **Cancel** Action.

***

## Dashboards

### Platform-independent

#### DashboardCreationWizardController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **CreateDashboard**.

Activated in the main Window. Supplies the **CreateDashboard** Action, allowing users to create dashboards.

**See Also:** [IModelOptionsDashboard.EnableCreation](xref:DevExpress.ExpressApp.SystemModule.IModelOptionsDashboard.EnableCreation) | [](xref:DevExpress.ExpressApp.DashboardView)

***

#### DashboardCustomizationController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **OrganizeDashboard**.

Activated in nested **DashboardOrganizer** Detail Views. Supplies the **OrganizeDashboard** Action, allowing users to organize dashboards.

**See Also:** [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) | [](xref:DevExpress.ExpressApp.DashboardView)

***

#### DashboardDeactivateItemsActionsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **OrganizeDashboard**.

Activated in Dashboard Views. Deactivates the **SaveAndClose** and **SaveAndNew** Actions in Views displayed on a dashboard.

**See Also:** [ModificationsController.SaveAndCloseAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndCloseAction) | [ModificationsController.SaveAndNewAction](xref:DevExpress.ExpressApp.SystemModule.ModificationsController.SaveAndNewAction) |[](xref:DevExpress.ExpressApp.DashboardView)

***

#### DashboardOrganizerHideToolbarController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated in nested **DashboardOrganizationItem** Views. Disables the Actions toolbar in the dashboard organizer.

**See Also:** [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) | [](xref:DevExpress.ExpressApp.DashboardView)

***

#### DashboardOrganizerItemsCollectionsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **DeleteItem**, **HideItemsFromDashboard**, **ShowItemsOnDashboard**.

Activated in nested **DashboardOrganizationItem** Views. Supplies Actions allowing users to show, hide, and delete dashboard View Items in a dashboard View.

**See Also:** [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) | [](xref:DevExpress.ExpressApp.DashboardView) | [](xref:DevExpress.ExpressApp.Editors.DashboardViewItem)

***

#### DeleteDashboardsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **DeleteDashboard**.

Activated in the main Window. Supplies the **DeleteDashboard** Action located in the **Tools** category. This Action invokes a popup dialog with a list of all dashboard views defined in the user's model differences. In this popup you can select one or more dashboards and click **Delete** to remove them. The `DeleteDashboardsController.CanDeleteParentGroup` property specifies whether or not the dashboard's parent group is deleted when you remove the last dashboard in this group. The **DeleteDashboard** Action is active when there are dashboards that can be deleted and the `EnableCreation` property of the **Options** | **Dashboards** node is set to `true` in the Application Model.

**See Also:** [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) | [](xref:DevExpress.ExpressApp.DashboardView)

***

#### ViewDashboardOrganizationItemController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated in **ViewDashboardOrganizationItem** Views. Refreshes the dashboard organizer when a dashboard View Item type changes.

**See Also:** [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) | [](xref:DevExpress.ExpressApp.DashboardView)

***

### Windows Forms

#### DashboardWinLayoutManagerController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated in Dashboard Views. Allows users to add new Views and remove existing Views from a dashboard with the Customization dialog.

**See Also:** [IModelView.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) | [](xref:DevExpress.ExpressApp.DashboardView) | [](xref:DevExpress.ExpressApp.Editors.DashboardViewItem)

***

## Debugging and Testing

### Platform-independent

#### ActionsInfoController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

A Diagnostic Controller implementing the `IDiagnosticController` interface. This Controller collects information on all Controllers of the current [Frame (Window)](xref:112608), the Controllers' Actions, the current [Template](xref:112609) and its [Action Containers](xref:112610), and the current [View](xref:112611) and its Editor(s). The `DiagnosticInfoController` adds the Single Choice Action Item exposed by this Controller to the **DiagnosticInfo** Action. When an user selects this item, the collected information is shown in an invoked window.

***

#### DiagnosticInfoProviderBase

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions:  none.

Activated in all windows and frames. `DiagnosticInfoProviderBase` is the base class for the [ActionsInfoController](#actionsinfocontroller), [ViewInfoController](#viewinfocontroller), and [ShowRulesController](xref:113142#showrulescontroller) Controllers. These Controllers provide items for the [DiagnosticInfoController](#diagnosticinfocontroller)'s **Diagnostic Info** Action. The `DiagnosticInfoProviderBase` class exposes members designed to create the **Diagnostic Info** Action's items and collect the information displayed when selecting these items.

**See Also:** [Determine Why an Action, Controller or Editor is Inactive](xref:112818) | [ActionBase.DiagnosticInfo](xref:DevExpress.ExpressApp.Actions.ActionBase.DiagnosticInfo)

***

#### DiagnosticInfoController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions:  **Diagnostic Info**.

Activated in all windows and frames. Finds all Controllers that implement the `IDiagnosticController` interface. These Controllers collect information on the required objects (Controllers, Actions, current Template, validation rules and so on). The `DiagnosticInfoController`'s **Diagnostic Info** Action, representing a Single Choice Action, contains the Single Choice Action Items that are exposed by Diagnostic Controllers that are found. When the **Diagnostic Info** Action's item is selected, a window with the information collected by the corresponding Controller is displayed. This information helps to find out why the Controller or Action is inactive or invisible.

**See Also:** [Determine Why an Action, Controller or Editor is Inactive](xref:112818) | [ActionBase.DiagnosticInfo](xref:DevExpress.ExpressApp.Actions.ActionBase.DiagnosticInfo)

***

#### ViewInfoController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

A Diagnostic Controller implementing the `IDiagnosticController` interface. This Controller collects information on the current View and its editor(s). The [DiagnosticInfoController](#diagnosticinfocontroller) adds the Single Choice Action Item exposed by this Controller to the **DiagnosticInfo** Action. When a user selects this item, the collected information is shown in an invoked window.

**See Also:** [Determine Why an Action, Controller or Editor is Inactive](xref:112818)

***

### ASP.NET Core Blazor

#### EasyTestAssistanceController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

For internal use. Implements functionally required to support `DetailPropertyEditor` in [EasyTest](xref:113211).

***

### Windows Forms

#### LookupControlFinderController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for Views displayed by `LookupPropertyEditor`. Discovers controls in pop-up Windows and supplies them to [EasyTest](xref:113211).

**See Also:** [Functional Testing](xref:113211)

***

#### WindowControlFinderController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **EasyTest Control**.

Activated in all Windows. Discovers controls in the current Window and supplies them to [EasyTest](xref:113211). Declares the **EasyTest Control** diagnostic Action, which lists all these controls.

**See Also:** [Functional Testing](xref:113211)

***

## Miscellaneous

### Platform-independent

#### ActionsCriteriaViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_. Actions: none.

Disables and enables Actions depending on their [ActionBase.TargetObjectsCriteria](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteria) and [ActionBase.TargetObjectsCriteriaMode](xref:DevExpress.ExpressApp.Actions.ActionBase.TargetObjectsCriteriaMode) property values.

***

#### DetailViewEditorActionController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions:  none.

Activated for Detail Views. Collects the Actions of the current Detail View's Items that implement the `IActionSource` interface and ensures that the Actions will be activated and can be executed. Actions are exposed by the `IActionSource.Actions` property.

***

#### DetailViewLinkController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. When a Detail View is invoked from a List View in a separate window, this Controller updates the List View if anything changes in the Detail View. For instance, when a Detail View's object is replaced with another (for example, using the **NextObject** Action), the focused object in the List View changes. When an object is modified or deleted in a Detail View, the List View's objects are updated as well. When an object is opened in a Detail View from a nested list view, all new objects created in this Detail View are automatically linked to the master object, which owns the collection bound to the nested List View. The **`DetailViewLinkController`** subscribes to the [IObjectSpace.Committed](xref:DevExpress.ExpressApp.IObjectSpace.Committed) event. In this event handler, an object matching the [DetailView.CurrentObject](xref:DevExpress.ExpressApp.DetailView.CurrentObject) is searched in the List View from which the current Detail View was opened. The found object is reloaded if the `DetailView.CurrentObject` is modified.

***

#### DialogController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions:  **DialogOK**, **DialogCancel**.

Activated in pop-up windows invoked by the [](xref:DevExpress.ExpressApp.Actions.PopupWindowShowAction). Contains the **DialogOK** and **DialogCancel** Actions.
You can add this Controller to a pop-up window when you create it using an Action's [](xref:DevExpress.ExpressApp.ShowViewParameters) object.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.DialogController) | [DialogController.AcceptAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.AcceptAction) | [DialogController.CancelAction](xref:DevExpress.ExpressApp.SystemModule.DialogController.CancelAction) | [Dialog Controller](xref:112805)

***

#### ExportController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **Export**.

Activated in all Views. The abstract base Controller for the [WinExportController](#winexportcontroller). Contains the **Export** Action which exports data from List View.
The Action is active in List Views when the [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) editor supports the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.ExportController) | [ExportController.ExportAction](xref:DevExpress.ExpressApp.SystemModule.ExportController.ExportAction) | [How to: Customize the Export Action Behavior](xref:113287)

***

#### FillActionContainersController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

When a Template is created, all its Action Containers are created as well. Then, the **FillActionContainers** Controller uses the [Application Model](xref:112580) to determine Actions that are to be displayed within Action Containers. In particular, the **ActionDesign** | **ActionToContainerMapping** node provides this information. Then, this Controller calls the Action Container's `Register` method for each Action to create the corresponding control. Action Containers create specific controls for each Action type.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.IModelActionToContainerMapping) | [Actions](xref:112622) | [Action Containers](xref:112610)

***

#### FocusDefaultDetailViewItemController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Extends the [Application Model](xref:112580)'s **DetailView** nodes with the `DefaultFocusedItem` property that specifies the property editor initially focused when the root Detail View is displayed. Note that the Detail View displayed with the List View (see [Display a Detail View with a List View](xref:404203)) is not a root, so the `DefaultFocusedItem` property makes no sense in this case. The following platform-specific Controller is derived from `FocusDefaultDetailViewItemController`: [WinFocusDefaultDetailViewItemController](#winfocusdefaultdetailviewitemcontroller).

**See Also:** [IModelDetailViewDefaultFocusedItem.DefaultFocusedItem](xref:DevExpress.ExpressApp.SystemModule.IModelDetailViewDefaultFocusedItem.DefaultFocusedItem) | [](xref:DevExpress.ExpressApp.Model.IModelDetailView) | [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)

***

#### HideActionsViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Deactivates the Actions that are listed in the **HiddenActions** child node of the current View's **View** node.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.IModelHiddenActions) | [](xref:DevExpress.ExpressApp.Model.IModelView)

***

#### ObjectMethodActionsViewController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: Actions, added with the **Action** Attribute.

Activated for all Views. Iterates through all business classes present in the Application Model's **BOModel** node, collects methods that are decorated with the **Action** attribute, and converts them to Simple Actions. Each Action is activated if the current View's object type corresponds to the class from which it was generated.

**See Also:** [](xref:DevExpress.Persistent.Base.ActionAttribute) | [](xref:DevExpress.ExpressApp.Actions.SimpleAction) | [](xref:402156) | [How to: Create an Action Using the Action Attribute](xref:112619)

***

#### RefreshController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **Refresh**.

Activated for all Views. Contains the **Refresh** Action, which is activated for root Views only. When executing this Action, the [BaseObjectSpace.Refresh](xref:DevExpress.ExpressApp.BaseObjectSpace.Refresh) method is called.

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.RefreshController) | [RefreshController.RefreshAction](xref:DevExpress.ExpressApp.SystemModule.RefreshController.RefreshAction)

***

#### ResetViewSettingsController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: **ResetViewSettings**.

Activated for all Views. Contains the **ResetViewSettings** Action, which re-opens the current View and resets all user customizations of the View's model. If you use the **ListViewAndDetailView** display mode, the **ResetViewSettings** Action is applied to both List and Detail Views unless the `AllowResetEditView` property is set to `false`. The Action is disabled (grayed out) if there are unsaved changes.

**See Also:** [BlazorResetViewSettingsController](#blazorresetviewsettingscontroller) | [List View Columns Customization](xref:113679) | [Detail View Layout Customization](xref:112817)

***

#### WindowTemplateController

Platform: platform-independent.

Assembly: _DevExpress.ExpressApp.v<:xx.x:>.dll_.

Actions: none.

Updates the current Window's caption and status messages. Exposes events and methods allowing you to customize and refresh caption and status messages. Has a WinForms-specific descendant - [WinWindowTemplateController](#winwindowtemplatecontroller).

**See Also:** [](xref:DevExpress.ExpressApp.SystemModule.WindowTemplateController) | [How to: Customize a Window Caption](xref:113252) | [How to: Customize Window Status Messages (WinForms)](xref:113253)

***

### ASP.NET Core Blazor

#### ActionHandleExceptionController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Handles exceptions that are thrown when XAF executes an Action.

***

#### BlazorResetViewSettingsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: inherited.

Blazor-specific [ResetViewSettingsController](#resetviewsettingscontroller) descendant. Changes the base controller's `AllowResetEditView` property to `false`. This way Detail Views are not affected when a user executes this action in [split views](xref:404203). To revert changes to a Detail View's layout, use the [Reset Layout](xref:404353) context menu action instead. **Reset View Settings** Action is available in record context menus (List Views):

![Context menu](~/images/blazor-reset-view-settings-action.png)

> [!NOTE]
> All actions that customize a List View are available in column header context menus. If you disable these menus (deactivate the [`DxGridListEditorColumnContextMenuController`](#dxgridlisteditorcolumncontextmenucontroller)), the **Reset View Settings** Action becomes unnecessary and XAF disables it too.


***

#### BlazorRibbonController 

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Configures the Ribbon UI and handles Ribbon merging between [`ApplicationRibbonWindowTemplate`](xref:403450#main-ribbon-form-template-applicationribbonwindowtemplate) and [`DetailRibbonFormTemplate`](xref:403450#detail-ribbon-form-template-detailribbonformtemplate)

***

#### CloseDetailViewController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: **Close Action**.

Activated for Detail Views. The **CloseAction** closes the current View.

***

#### ConfirmationActionRegistrationController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Implements the [IModelActionBlazor.ConfirmUnsavedChanges](xref:DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.ConfirmUnsavedChanges) functionality and registers Actions whose `ConfirmUnsavedChanges` property is set to `true`.

***

#### ConfirmationDetailViewController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Implements "unsaved changes" confirmation dialog functionality in Detail Views.

***

#### ConfirmationListViewController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Implements "unsaved changes" confirmation dialog functionality in List Views.

***

#### ConfirmationUnsavedLinkedObjectController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Implements "unsaved changes" confirmation dialog functionality in nested List Views.

***

#### CustomizeActionControlController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Supports @DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.AdaptivePriority and @DevExpress.ExpressApp.Blazor.SystemModule.IModelActionBlazor.CustomCSSClassName in Actions displayed by the @DevExpress.Blazor.DxToolbar control.

***

#### CustomizeBlazorActionContainerViewItemController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated in Composite Views. Implements functionality required for @DevExpress.ExpressApp.Editors.ActionContainerViewItem.

***

#### DetailViewRefreshController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Forces an update for neighboring property editors after a value change in the current property editor.

***

#### DisableDashboardLayoutEditorController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Dashboard Views. Disables [runtime layout customization](xref:404353) in the current Dashboard View and its nested Detail Views.

***

#### DisableLayoutEditorController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Disables [runtime layout customization](xref:404353) in specific Views.

***

#### DisableNestedLayoutEditorController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Detail Views. Disables [runtime layout customization](xref:404353) in nested Detail Views.

***

#### LayoutEditorConfirmationController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for Composite Views. Implements "unsaved changes" confirmation dialog functionality for [runtime layout customization](xref:404353).

***

#### ManageActionVisibilityController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Manages Toolbar visibility in selection-dependent Actions in List Views.

***

#### ObjectModelController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Adds the **Customize** button to the List View's @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor Column Chooser and to the Detail View's [Customization Form](xref:404353). When a user clicks the button, XAF displays the **Object Model** dialog window where you can hide or display properties.

**See also:** [](xref:403217)

***

#### PopupWindowTemplateClosingController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Manages the **Close** button's visibility in a pop-up window. When a user clicks the button, XAF executes the `ClosePopupWindow` method. Your can override this method to implement your own logic:

```csharp
using DevExpress.ExpressApp.Blazor.SystemModule;
using DevExpress.ExpressApp;
using YourApplicationName.Module.BusinessObjects;

namespace YourApplicationName.Blazor.Server.Controllers;
public class PopupWindowTemplateClosingControllerExample : PopupWindowTemplateClosingController {
    protected override bool ClosePopupWindow(Window popupWindow) {
        if (popupWindow.View.CurrentObject is Employee employee && employee.FirstName == "James") {
            return false;
        }
        return base.ClosePopupWindow(popupWindow);
    }
}
```

**See Also:** [](xref:DevExpress.ExpressApp.Blazor.SystemModule.PopupWindowTemplateClosingController)

***

#### PopupWindowTemplateSizeController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Manages drag and resize settings of a pop-up window.

**See Also:** [](xref:DevExpress.ExpressApp.Blazor.SystemModule.PopupWindowTemplateSizeController)

***

#### PrimaryToolbarItemsController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Sets `RenderStyle` to `Primary` for several Actions (such as **Logon** and **Save**).

***

#### SaveModelDifferencesController

Platform: ASP.NET Core Blazor.

Assembly: _DevExpress.ExpressApp.Blazor.v<:xx.x:>.dll_.

Actions: none.

Activated for List Views. Saves [user differences (individual user settings)](xref:112580#application-model-layers). For example, saved information includes filter conditions and sort order in List Views.

***

### Windows Forms

#### AboutInfoController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **AboutInfo**.

Activated in the main window. Contains the **About Info** Action. In Windows Forms applications, this Action presents general information on the current application collected from the Application Model by this Controller.

**See Also:** [Application Personalization](xref:113445)

***

#### AboutInfoFormController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated in the Detail Views of the **AboutInfo** objects. Sets up the About window:

* Disables the ability to customize layouts.
* Fixes the window's width according to the Logo image's width.
* Removes the Static Image [View Item](xref:112612) if the image is not specified.
* Enables the [Label Emphasis](xref:113130) feature to divide the About text into multiple strings.

***

#### AsyncLoadingCancelationController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Cancels the [asynchronous loading](xref:401747) of data in a View when a user closes it. This Controller allows you to show a confirmation message when you close a View in the UI.

**See Also:** [How to: Customize Asynchronous Data Loading Behavior and UI](xref:401750)

***

#### AsyncLoadingIndicationController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Shows the [Overlay Form](xref:112680) and disables built-in Actions while an asynchronous operation is in progress.

**See Also:** [How to: Customize Asynchronous Data Loading Behavior and UI](xref:401750)

***

#### ChooseSkinController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **ChooseSkin**.

Activated in the main window if the [UseLightStyle](xref:DevExpress.ExpressApp.Win.WinApplication.UseLightStyle) property is `false`. Otherwise, the [ConfigureSkinController](#configureskincontroller) is activated instead.

Contains the **ChooseSkin** Action. This Action allows users to apply a predefined skin to the application. The selected skin is stored in the [Skin](xref:DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsSkin.Skin) property of the Application Model's **Options** node.

**See Also:** [Application Model Basics](xref:112580) | [Application Model Structure](xref:112580)

***

#### ConfigureSkinController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **ConfigureSkin**.

Activated in the main window if the [UseLightStyle](xref:DevExpress.ExpressApp.Win.WinApplication.UseLightStyle) property is `true`. Otherwise, the [ChooseSkinController](#chooseskincontroller) is activated instead.

Contains the **ConfigureSkin** Action. This Action allows users to apply a predefined skin to the application. Users can also select a palette if a skin supports palettes. The selected skin is stored in the [Skin](xref:DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsSkin.Skin) property of the Application Model's **Options** node. The selected palette is stored in the [Palette](xref:DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsPalette.Palette) property of the Application Model's **Options** node.

**See Also:** [Application Model Basics](xref:112580) | [Application Model Structure](xref:112580)

***

#### CloseMdiChildWindowController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win<:xx.x:>.dll_.

Actions: none.

Activated in child Windows when [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) is used. Prohibits closing a child Window while its View is changing and closes the Window when its View is closed.

***

#### CloseWindowController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win<:xx.x:>.dll_.

Actions: **Close**.

Activated in child Windows. The **Close** Action closes the current window. It is active when a current window contains a View.

***

#### DockPanelsVisibilityController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for all windows. Creates a [](xref:DevExpress.ExpressApp.Actions.SingleChoiceAction) in the **Panels** category for each dock panel located in the current window if the current window [Template](xref:112609) implements the `IDockManagerHolder` interface. The created Actions allow you to change dock panel visibility to `Visible`, `AutoHide`, or `Hidden`.

**See Also:** [Template Customization](xref:112696)

***

#### EditModelController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **EditModel**.

Activated in all windows. Contains the **EditModel** Action. This Action allows users to invoke the [Model Editor](xref:112582) at runtime. When the [Security System](xref:113366) is used, this Action is deactivated if the current user does not have permission to edit the Application Model.

***

#### ExitController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **Exit**.

Contains the **Exit** Action, which is used to close the application.

***

#### HtmlFormattingController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for all Views. Adds the **EnableHtmlFormatting** property to the **Options** node. When this property is set to `true`, HTML formatting of the Property Editor captions, List View column captions, and Static View Item text are rendered. When this property is set to `false`, HTML formatting is not supported.

**See Also:** [IModelOptionsEnableHtmlFormatting.EnableHtmlFormatting](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsEnableHtmlFormatting.EnableHtmlFormatting) | [](xref:DevExpress.ExpressApp.Model.IModelOptions) | [How to: Apply HTML Formatting to Windows Forms XAF UI Elements](xref:113130)

***

#### LockController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for all Views. Locks modifying an object, if it is currently being modified in another View.

**See Also:** [Optimistic Concurrency Control](xref:113596)

***

#### MdiTabImageController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for child [Windows](xref:112608) when the [](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy) is used in [MdiMode.Tabbed](xref:DevExpress.ExpressApp.Win.Templates.MdiMode.Tabbed) mode. Sets tab images accordingly to the displayed Views.

**See Also:** [UIType.TabbedMDI](xref:DevExpress.ExpressApp.UIType.TabbedMDI)

***

#### OpenObjectController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **OpenObject**.

Activated for all Views. The Action is executed after you:

* Focus a reference property editor and click the Action's button on the toolbar.
* Hold SHIFT+CTRL and click a reference property editor.
* Focus an editor and press Shift+Ctrl+Enter.

In Detail Views, this Controller operates with Property Editors inherited from the [](xref:DevExpress.ExpressApp.Win.Editors.WinPropertyEditor) class; if the currently focused editor is bound to a reference property, the **OpenObject** Action invokes the referenced object Detail View. In List Views, this Controller operates when the current [ListView.Editor](xref:DevExpress.ExpressApp.ListView.Editor) is [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor);  the **OpenObject** Action invokes the Detail View of the object from the focused cell.

> [!NOTE]
> * The **OpenObject** Action is inactive when the List View is in [DataView](xref:113683), [ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) mode.
> * The **OpenObject** Action does not work with a reference property in [](xref:DevExpress.ExpressApp.TreeListEditors.Win.TreeListEditor).
> * The [IModelMemberViewItem.View](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.View) property is ignored when you invoke the Detail View from the List View through the Ctrl+Shift+Click combination.

To specify the View invoked on the **OpenObject** Action execution, use the **OpenObjectController.CustomOpenObject** event, as shown in the [How to specify what DetailView is shown by the Open Related Record action execute or ctrl shift key combination click](https://supportcenter.devexpress.com/ticket/details/t437813/how-to-specify-what-detailview-is-shown-by-the-open-related-record-action-execute-or) Support Center ticket.

***

#### PrintingController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: **PageSetup**, **Print** and **PrintPreview**.

Activated for Detail Views whose control implements the [](xref:DevExpress.XtraPrinting.IPrintable) interface and List Views whose [List Editor](xref:113189) implements the [](xref:DevExpress.ExpressApp.SystemModule.IExportable) interface. Provides Actions that allow users to print the current View.

**See Also:** [](xref:DevExpress.ExpressApp.Win.SystemModule.PrintingController)

***

#### VersionsCompatibilityController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated in all Views. When working with an application, its version and database can be updated. This can corrupt the database. This Controller checks the application and database versions compatibility periodically during the application run. If a version mismatch is found, a warning window is invoked.

***

#### WaitCursorController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Changes the cursor to the hour glass mode while an Action is executing.

***

#### WinExportController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

The Windows Forms-specific descendant of the [ExportController](#exportcontroller). Creates a file stream for the exported data.

**See Also:** [](xref:DevExpress.ExpressApp.Win.SystemModule.WinExportController)

***

#### WinFocusDefaultDetailViewItemController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

The platform-specific descendent of the [FocusDefaultDetailViewItemController](#focusdefaultdetailviewitemcontroller).

***

#### WinFocusListEditorControlController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated in all Windows. When the currently displayed View changes to a List View, focuses the List Editor's control.

**See Also:** [List Editors](xref:113189)

***

#### WinLayoutManagerController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Sets up the editor's **Customization** form and supports its functionality. To invoke this form, select **Customize Layout** in the detail form's context menu.

**See Also:** [View Items Layout Customization](xref:112817)

***

#### WinWindowTemplateController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

A WinForms-specific descendant of the [WindowTemplateController](#windowtemplatecontroller). Handles events of the [](xref:DevExpress.XtraBars.Docking2010.DocumentManager) to update the current Window's caption.

***

#### XtraGridInLookupController

Platform: Windows Forms.

Assembly: _DevExpress.ExpressApp.Win.v<:xx.x:>.dll_.

Actions: none.

Activated for all Views. Intended for internal use. Sets up the `XtraGrid` control used in the Lookup Property Editor's lookup window in Detail and List Views.

***
