---
uid: DevExpress.ExpressApp.Win.SystemModule.IModelRootGroupsStyle.RootGroupsStyle
name: RootGroupsStyle
type: Property
summary: Specifies the style of the [navigation](xref:113198) root group.
syntax:
  content: RootGroupsStyle RootGroupsStyle { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Win.Templates.Navigation.RootGroupsStyle
    description: The [](xref:DevExpress.ExpressApp.Win.Templates.Navigation.RootGroupsStyle) enumeration value which specifies the style of the navigation root group.
seealso: []
---
In the `OutlookSimple` or `OutlookAnimated` modes, the [](xref:DevExpress.XtraBars.Navigation.OfficeNavigationBar) control is used to display root navigation groups in addition to the [](xref:DevExpress.XtraNavBar.NavBarControl).

![OutlookStyleMainRibbonForm](~/images/outlookstylemainribbonform123038.png)

Use the [Model Editor](xref:112582) invoked for the WinForms application project to change the `RootGroupsStyle` value.

![Model_RootGroupsStyle](~/images/model_rootgroupsstyle123223.png)

Setting this property to the `OutlookSimple` or `OutlookAnimated` has effect under the following conditions.

* The [IModelRootNavigationItems.NavigationStyle](xref:DevExpress.ExpressApp.SystemModule.IModelRootNavigationItems.NavigationStyle) property is set to `NavBar`.
* The [IModelOptionsWin.FormStyle](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.FormStyle) property is set to `Ribbon`.
* The [IModelOptionsWin.UIType](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.UIType) property is set to `SingleWindowSDI` or `MultipleWindowSDI`.

Otherwise, the `Standard` style is always used.
