---
uid: "113316"
seealso: []
title: "Application Model: Built-in Node Generators"
owner: Ekaterina Kiseleva
---
# Application Model: Built-in Node Generators

Internally, XAF modules use approaches described in the [Extend and Customize the Application Model in Code](xref:112810) topic to generate the Application Model content. This topic provides a list of built-in Node Generators. You can use this list when customizing the application model by implementing a Generator Updater. Here, you can find out what Node Generators are available for customization.

## Node Generators in the System Module
{|
|-

! Node Generator
! Target Model Interface
! Description
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ImageSourceNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelImageSources)
| Generates the following child nodes of the **ImageSources** node:
* the "Images" [](xref:DevExpress.ExpressApp.Model.IModelFileImageSource) node
* the [](xref:DevExpress.ExpressApp.Model.IModelAssemblyResourceImageSource) nodes for each referenced module assembly
* the "DevExpress.Images.v<:xx.x:>" @DevExpress.ExpressApp.Model.IModelDevExpressImagesAssemblyImageSource node for the _DevExpress.Images.v<:xx.x:>_ assembly
|-

| [](xref:DevExpress.ExpressApp.SystemModule.ModelActionContainersGenerator)
| [](xref:DevExpress.ExpressApp.SystemModule.IModelActionToContainerMapping)
| Generates child nodes of the **ActionDesign** | **ActionToContainerMapping** node. 
Collects [IModelAction.Category](xref:DevExpress.ExpressApp.Model.IModelAction.Category) values specified for **ActionDesign** | **Actions** nodes and generates [](xref:DevExpress.ExpressApp.SystemModule.IModelActionContainer) node for each category found. Each **ActionContainer** node contains [](xref:DevExpress.ExpressApp.SystemModule.IModelActionLink) nodes specifying Actions linked to the Action Container.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelActionsNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelActions)
| Generates child nodes of the **ActionDesign** | **Actions** node. Collects Controllers from the **Controllers** node, and gets their owned Actions via the [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) property. Adds [](xref:DevExpress.ExpressApp.Model.IModelAction) nodes that represent found actions. An [](xref:DevExpress.ExpressApp.Model.IModelChoiceActionItems) child node is additionally created for [](xref:DevExpress.ExpressApp.Actions.ChoiceActionBase) Actions,
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelClassNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelBOModel)
| Generates child nodes of the **BOModel** node. Adds an [](xref:DevExpress.ExpressApp.Model.IModelClass) node for each business class. Initializes these **Class** node's properties: [IModelClass.Caption](xref:DevExpress.ExpressApp.Model.IModelClass.Caption), [IModelClass.DefaultListView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultListView), [IModelClass.DefaultLookupListView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultLookupListView), [IModelClass.DefaultDetailView](xref:DevExpress.ExpressApp.Model.IModelClass.DefaultDetailView), and properties whose values are specified in code via the [](xref:DevExpress.Xpo.CustomAttribute).
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelBOModelMemberNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelBOModelClassMembers)
| Generates child nodes of **BOModel** | **OwnMembers** nodes. Gets a public members list from the business class' metadata information. Initializes the [](xref:DevExpress.ExpressApp.Model.IModelMember) nodes' properties with values specified in code via [Data Annotations in Data Model](xref:112701) applied to business class members, e.g [](xref:DevExpress.Xpo.CustomAttribute), [](xref:DevExpress.Persistent.Base.IndexAttribute), [](xref:DevExpress.Persistent.Base.LookupEditorModeAttribute), [](xref:DevExpress.Persistent.Base.ImagesForBoolValuesAttribute), [](xref:DevExpress.Persistent.Base.CaptionsForBoolValuesAttribute), [](xref:DevExpress.Persistent.Base.ImageEditorAttribute), [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute), etc.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelChoiceActionItemsNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelChoiceActionItems)
| Generates child nodes of the [!include[Node_Action](~/templates/node_action111373.md)] | **ChoiceActionItems** nodes. Adds [](xref:DevExpress.ExpressApp.Model.IModelChoiceActionItem) nodes that represent items of the Choice Action.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelControllerActionsNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelControllerActions)
| Generates child nodes of the **ActionDesign** | **Controllers** | **Controller** | **Actions** nodes. Collects Actions of the current Controller from the [](xref:DevExpress.ExpressApp.Model.IModelActions) node.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelControllersNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelControllers)
| Generates child nodes of the **ActionDesign** | **Controllers** node. Adds an [](xref:DevExpress.ExpressApp.Model.IModelViewController), [](xref:DevExpress.ExpressApp.Model.IModelWindowController) or [](xref:DevExpress.ExpressApp.Model.IModelController) node for each registered Controller, depending on the Controller type. Adds the [](xref:DevExpress.ExpressApp.Model.IModelControllerActions) child node for Controllers exposing a non-empty [Controller.Actions](xref:DevExpress.ExpressApp.Controller.Actions) Actions list.
|-

| [](xref:DevExpress.ExpressApp.SystemModule.ModelCreatableItemsGenerator)
| [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItems)
| Generates child nodes of the **CreatableItems** node. Adds an [](xref:DevExpress.ExpressApp.SystemModule.IModelCreatableItem) node for each business class having the [IModelClass.IsCreatableItem](xref:DevExpress.ExpressApp.Model.IModelClass.IsCreatableItem) property set to **True**.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewItemsNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelViewItems)
| Generates child nodes of the **Views** | **View** | **Items** node. If the parent **View** node is [](xref:DevExpress.ExpressApp.Model.IModelObjectView), adds [](xref:DevExpress.ExpressApp.Model.IModelPropertyEditor) nodes for members of the current object that should be visible. 
Separate **PropertyEditor** nodes are generated for aggregated objects' members if this option is enabled via the [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute) attribute. An example of implementing a Generator Updater for this Node Generator is provided in the [](xref:405483) topic.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelDetailViewLayoutNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelViewLayout)
| Generates child nodes of the **Views** | **View** | **Layout** node. Creates the layout structure of the current View. The rules of generating a default layout are described in the [View Items Layout Customization](xref:112817) topic. An example of implementing a Generator Updater for this Node Generator is provided in the [](xref:405483) topic.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelListViewColumnsNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelColumns)
| Generates child nodes of the [!include[Node_Views_ListView_Columns](~/templates/node_views_listview_columns111387.md)] node. Adds [](xref:DevExpress.ExpressApp.Model.IModelColumn) nodes that represent columns of the current List View. The rules for generating the default column set are described in the [List View Column Generation](xref:113285) topic.
|-

| [](xref:DevExpress.ExpressApp.SystemModule.ModelListViewFiltersGenerator)
| [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilters)
| Generates child nodes of the **View** | **ListView** | **Filters** node. Collects filters specified for the current List View's business class via the [](xref:DevExpress.ExpressApp.SystemModule.ListViewFilterAttribute) attributes. Creates the [](xref:DevExpress.ExpressApp.SystemModule.IModelListViewFilterItem) for each filter. An example of implementing a Generator Updater for this Node Generator is provided in the [Filters Application Model Node](xref:112992) topic.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationGroupGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup)
| Generates child nodes of the **Localization** | **LocalizationGroup** node. Adds [](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem) and nested [](xref:DevExpress.ExpressApp.Model.IModelLocalizationGroup) nodes of the current localization group based on registered **IXafResourceLocalizer** objects.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelLocalizationNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelLocalization)
| Generates first-level child nodes ([](xref:DevExpress.ExpressApp.Model.IModelLocalizationItem) nodes) of the **Localization** node, based on registered **IXafResourceLocalizer** objects. The example of implementing a Generator Updater for this Node Generator is provided in the [EnumDescriptor.GenerateDefaultCaptions](xref:DevExpress.ExpressApp.Utils.EnumDescriptor.GenerateDefaultCaptions*) topic.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelOptionsNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelOptions)
| This is an empty generator that does nothing. However, as it is attached to the **Options** node, you can implement a Generator Updater for this Generator, and customize the **Options** node.
|-

| [](xref:DevExpress.ExpressApp.Editors.ModelRegisteredViewItemsGenerator)
| [](xref:DevExpress.ExpressApp.Editors.IModelRegisteredViewItems)
| Generates child nodes of the **ViewItems** node. Adds [](xref:DevExpress.ExpressApp.Editors.IModelRegisteredViewItems) and [](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditors) nodes, based on registered Property Editors.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.ModelViewsNodesGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelViews)
| Generates child nodes of the **Views** node. Adds an [](xref:DevExpress.ExpressApp.Model.IModelDetailView) and two [](xref:DevExpress.ExpressApp.Model.IModelListView) nodes for each class defined in the [](xref:DevExpress.ExpressApp.Model.IModelBOModel) node. One of the generated **ListView** nodes defines a general-purpose List View, and another - a Lookup List View. An example of implementing Generator Updaters for this Node Generator is provided in the [How to: Create Additional ListView Nodes in Code using a Generator Updater](xref:113315) topic.
|-

| [](xref:DevExpress.ExpressApp.SystemModule.NavigationItemNodeGenerator)
| [](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems)
| Generates child nodes of the [!include[Node_NavigationItemsRoot](~/templates/node_navigationitemsroot111377.md)] node. Adds [](xref:DevExpress.ExpressApp.SystemModule.IModelNavigationItem) nodes for business classes that have the [IModelClassNavigation.IsNavigationItem](xref:DevExpress.ExpressApp.SystemModule.IModelClassNavigation.IsNavigationItem) property set to **true** in the corresponding **BOModel** | **_\<Class\>_** node.
|-

| [](xref:DevExpress.ExpressApp.Model.NodeGenerators.TemplatesModelNodeGenerator)
| [](xref:DevExpress.ExpressApp.Model.IModelTemplates)
| This is an empty generator that does nothing. However, as it is attached to the **Templates** node, you can implement a Generator Updater for this Generator, and customize the **Templates** node.
|}

## Node Generators in Extra Modules
| Node Generator | Module | Target Model Interface | Description |
|---|---|---|---|
| [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceRulesModelNodesGenerator) | [Conditional Appearance](xref:113286) | [](xref:DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRules) | Generates child nodes of a **BOModel** \| **_\<Class\>_** \| **AppearanceRules** node. Collects [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) attributes applied in a business class code and adds corresponding [](xref:DevExpress.ExpressApp.ConditionalAppearance.IModelAppearanceRule) nodes. |
| [](xref:DevExpress.ExpressApp.FileAttachments.Win.FileTypeFiltersNodesGenerator) | [File Attachments](xref:112781) (Windows Forms) | [](xref:DevExpress.ExpressApp.FileAttachments.Win.IModelFileTypeFilters) | Generates child nodes of a **BOModel** \| **_\<Class\>_** \| **FileTypeFilters** node.  Collects [](xref:DevExpress.Persistent.Base.FileTypeFilterAttribute) attributes applied in the code of business classes, and adds corresponding [](xref:DevExpress.ExpressApp.FileAttachments.Win.IModelFileTypeFilter) nodes. |
| [](xref:DevExpress.ExpressApp.Validation.ModelValidationContextsNodeGenerator) | [Validation](xref:113684) | [](xref:DevExpress.ExpressApp.Validation.IModelValidationContexts) | Generates child nodes of the **Validation** \| **Contexts** node. Uses [IRuleBaseProperties.TargetContextIDs](xref:DevExpress.Persistent.Validation.IRuleBaseProperties.TargetContextIDs) values from the **Validation** \| **Rules** \| **Rule** nodes to collect Validation Contexts. Adds an [](xref:DevExpress.ExpressApp.Validation.IModelValidationContext) node for each Context. |
| [](xref:DevExpress.ExpressApp.Validation.ModelValidationRulesNodeGenerator) | [Validation](xref:113684) | [](xref:DevExpress.ExpressApp.Validation.IModelValidationRules) | Generates child nodes of the **Validation** \| **Rules** node. Collects Validation Rules specified in code and adds corresponding [](xref:DevExpress.ExpressApp.Validation.IModelRuleBase) nodes. |
