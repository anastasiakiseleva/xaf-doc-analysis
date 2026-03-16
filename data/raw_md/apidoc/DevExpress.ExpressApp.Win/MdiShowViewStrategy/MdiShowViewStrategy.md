---
uid: DevExpress.ExpressApp.Win.MdiShowViewStrategy
name: MdiShowViewStrategy
type: Class
summary: A Show View Strategy that uses a multiple document interface and can be used as an alternative to the default [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy).
syntax:
  content: 'public class MdiShowViewStrategy : WinShowViewStrategyBase'
seealso:
- linkId: DevExpress.ExpressApp.Win.MdiShowViewStrategy._members
  altText: MdiShowViewStrategy Members
- linkId: "11362"
---
The built-in [MainForm Template](xref:112609) includes a [](xref:DevExpress.XtraBars.Docking2010.DocumentManager) component. The **DocumentManager** is a non-visual object that displays content via Documents. Documents can be presented in different ways based on the DocumentManager's view. There are two Document Manager view types: [](xref:DevExpress.XtraBars.Docking2010.Views.NativeMdi.NativeMdiView) and [](xref:DevExpress.XtraBars.Docking2010.Views.Tabbed.TabbedView). The **MdiShowViewStrategy** uses the **DocumentManager** for showing XAF Views. Its [MdiShowViewStrategy.MdiMode](xref:DevExpress.ExpressApp.Win.MdiShowViewStrategy.MdiMode) property value is used to set the **DocumentManager**'s view. The following values are possible:

Tabbed
:   When the `MdiMode` property is set to [MdiMode.Tabbed](xref:DevExpress.ExpressApp.Win.Templates.MdiMode.Tabbed), the Document Manager uses the Tabbed MDI view. This means that [Views](xref:112611) are invoked in separate tabs:
    
    ![MdiModeTabbed](~/images/mdimodetabbed116706.png)
    
    In this mode, the **MdiShowViewStrategy** supports docking. Users can dock, group and arrange tabs or windows as desired. You can also Shift+Click a navigation item or an object reference, and the corresponding View will be invoked in a new window. Pressing Ctrl+Tab activates a [Document Selector](xref:11362). It allows you to switch between Views easily. To learn more about the capabilities that are provided in the Document Manager together with a DockManager, refer to the [Interaction with Dock Panels](xref:11363) topic. In addition, try the **Ribbon, Toolbar & Docking** | **Tutorials** | **Document Manager** Demo supplied with the DXperience installation. The **MdiShowViewStrategy** saves the arrangement of the open tabs when closing the application and restores them when re-opening the application. For optimal performance of the tabbed mode, delayed loading is implemented for restored tabs. This means that only controls of the active tab are created on application startup. At the same time, you can refuse saving the tabs layout by setting the **RestoreTabbedMdiLayout** property of the **Options** node to **false** in the Model Editor.
    
    > [!NOTE]
    > In the **Tabbed** mode, bar items from a child form are merged with bar items from a parent form. Merging is performed based on captions of the items (see [MDI Merging](xref:1099)). When [localizing](xref:113298), ensure that you specify different localized values for Action Container captions. Otherwise, unwanted Action duplication may occur.

Standard
:   When the `MdiMode` property is set to [MdiMode.Standard](xref:DevExpress.ExpressApp.Win.Templates.MdiMode.Standard), the Document Manager uses the Native MDI view. This means that [Views](xref:112611) are invoked in separate Windows:
    
    ![MdiModeStandard](~/images/mdimodestandard116705.png)
    
    > [!NOTE]
    > Model Editor prohibits using the **Standard** mode together with the [Ribbon](xref:404212) interface. The Document Manager has not been thoroughly tested for this configuration as we have found it much less usable than others. This configuration can potentially lead to errors. In conjunction with the Ribbon, the **Tabbed** mode provides better usability.

You can access the **DocumentManager** to customize its default settings. To do this, cast the Main Form Template by the **IDocumentsHostWindow** interface and get the value of its **DocumentManager** property. To see an example, refer to the [How to: Access the Document Manager](xref:113443) topic.

By default, **XAF** Windows Forms applications use the [](xref:DevExpress.ExpressApp.Win.ShowInMultipleWindowsStrategy). To use another Strategy, specify the [Application Model](xref:112580)'s [IModelOptionsWin.UIType](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.UIType) property of the Application | Options node. Alternatively, you can manually instantiate the required Strategy and assign it to the [XafApplication.ShowViewStrategy](xref:DevExpress.ExpressApp.XafApplication.ShowViewStrategy) property.

For general information on Show View Strategies, refer to the [](xref:DevExpress.ExpressApp.ShowViewStrategyBase) class description.
