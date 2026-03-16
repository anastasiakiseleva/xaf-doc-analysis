---
uid: "403535"
seealso: []
title: "Application Model: Built-in Interfaces"
owner: Eugenia Simonova
---
# Application Model: Built-in Interfaces

This topic lists [Application Model](xref:112579) interfaces and extenders shipped with XAF. XAF uses extenders to add properties to Application Model nodes. 

{|
|-
! Interface
! Description
! Extenders
|-

| @DevExpress.ExpressApp.Model.IModelAction
| Contains [Action](xref:112622) settings.
| @DevExpress.ExpressApp.Validation.IModelActionValidationContexts
|
-

| @DevExpress.ExpressApp.Model.IModelActionContainerViewItem
| Defines a View Item that displays an [Action Container](xref:112610).
| 
|-

| @DevExpress.ExpressApp.Model.IModelActionDesign
| Contains the [Actions](xref:112622), [Action Containers](xref:112610), [Controllers](xref:112621), and [DisableReasons](xref:DevExpress.ExpressApp.Model.IModelDisableReasons) nodes.
| @DevExpress.ExpressApp.SystemModule.IModelActionDesignContainerMapping
|-

| @DevExpress.ExpressApp.Model.IModelApplication
| Contains general information about an application.
| @DevExpress.ExpressApp.SystemModule.IModelApplicationCreatableItems,

@DevExpress.ExpressApp.SystemModule.IModelApplicationNavigationItems,

@DevExpress.ExpressApp.Validation.IModelApplicationValidation

|-

| @DevExpress.ExpressApp.Chart.IModelChartSettings 
| Contains the [Chart List Editor](xref:113302#chart-list-editors) settings in WinForms.

|-

| @DevExpress.ExpressApp.Model.IModelClass
| Defines a persistent class from the Business Model and provides access to its members.
| @DevExpress.ExpressApp.SystemModule.IModelClassShowAutoFilterRow,

  @DevExpress.ExpressApp.SystemModule.IModelClassShowFindPanel,

  @DevExpress.ExpressApp.SystemModule.IModelClassNewItemRow,

  @DevExpress.ExpressApp.SystemModule.IModelClassNavigation,

  @DevExpress.ExpressApp.Model.IModelClassReportsVisibility,

  @DevExpress.ExpressApp.CloneObject.IModelClassCloneable,

  @DevExpress.ExpressApp.FileAttachments.Win.IModelCommonFileTypeFilters,

  @DevExpress.ExpressApp.ConditionalAppearance.IModelConditionalAppearance

|-

| @DevExpress.ExpressApp.Model.IModelColumn
| Defines a column that displays a particular property.
| @DevExpress.ExpressApp.SystemModule.IModelPropertyEditorLinkView,

@DevExpress.ExpressApp.Win.SystemModule.IModelColumnWin,

@DevExpress.ExpressApp.TreeListEditors.Win.IModelColumnTreeListWin

|-

| @DevExpress.ExpressApp.Model.IModelDetailView
| Defines a Detail View of a specific business class.
| @DevExpress.ExpressApp.SystemModule.IModelDetailViewDefaultFocusedItem,

@DevExpress.ExpressApp.SystemModule.IModelViewHiddenActions,

@DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutManagerDetailViewOptions,

@DevExpress.ExpressApp.Win.SystemModule.IModelPrintingSettings
|-

| @DevExpress.ExpressApp.Model.IModelLayoutGroup
| Defines the layout of View Items that belong to a particular group.
| @DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutGroup
|-

| @DevExpress.ExpressApp.Model.IModelLayoutItem
| Defines the View Item layout in a Detail View. 
| @DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutItem
|-

| @DevExpress.ExpressApp.Model.IModelListView
| Defines a business class List View.
| @DevExpress.ExpressApp.Chart.IModelChartListView,

@DevExpress.ExpressApp.PivotGrid.IModelPivotListView,

@DevExpress.ExpressApp.SystemModule.IModelListViewFilter,

@DevExpress.ExpressApp.SystemModule.IModelViewHiddenActions,

@DevExpress.ExpressApp.SystemModule.IModelListViewPreviewColumn,

@DevExpress.ExpressApp.SystemModule.IModelListViewShowAutoFilterRow,

@DevExpress.ExpressApp.SystemModule.IModelListViewShowFindPanel,

@DevExpress.ExpressApp.SystemModule.IModelListViewNewItemRow,

@DevExpress.ExpressApp.Win.SystemModule.IModelPrintingSettings,

@DevExpress.ExpressApp.Scheduler.IModelListViewScheduler,

@DevExpress.ExpressApp.FileAttachments.Win.IModelCommonFileTypeFilters,

|-

| @DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems
| Specifies the [Navigation](xref:113198) Action structure.
| @DevExpress.ExpressApp.ReportsV2.IModelNavigationItemsForReports,

@DevExpress.ExpressApp.ViewVariantsModule.IModelNavigationItemsVariantSettings,

|-

| @DevExpress.ExpressApp.Model.IModelOptions
| Allows you to edit different UI settings.
| @DevExpress.ExpressApp.SystemModule.IModelOptionsDashboards,

 @DevExpress.ExpressApp.Win.SystemModule.IModelApplicationOptionsSkin,

 @DevExpress.ExpressApp.Win.SystemModule.IModelOptionsEnableHtmlFormatting,

 @DevExpress.ExpressApp.Win.SystemModule.IModelPrintingSettings,

@DevExpress.ExpressApp.Scheduler.Win.IModelOptionsScheduler,

@DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin,

@DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutManagerOptions,

@DevExpress.ExpressApp.FileAttachments.Win.IModelOptionsFileAttachment
|-

| @DevExpress.ExpressApp.Model.IModelPropertyEditor
| Defines a [Property Editor](xref:113097) for the current property.
| @DevExpress.ExpressApp.SystemModule.IModelPropertyEditorLinkView
|-

| @DevExpress.ExpressApp.Model.IModelTabbedGroup
| Defines the View Items layout within a tabbed group.
| @DevExpress.ExpressApp.Model.IModelLayoutElementWithCaption
|-


| @DevExpress.ExpressApp.Model.IModelView
| The base interface for @DevExpress.ExpressApp.Model.IModelListView, @DevExpress.ExpressApp.Model.IModelDetailView, and @DevExpress.ExpressApp.Model.IModelDashboardView.
| @DevExpress.ExpressApp.ViewVariantsModule.IModelViewVariants,

@DevExpress.ExpressApp.SystemModule.IModelViewHiddenActions
|}
