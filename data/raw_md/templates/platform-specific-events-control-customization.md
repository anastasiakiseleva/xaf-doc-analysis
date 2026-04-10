## Platform-Specific Events for Control Customization

In Windows Forms, a View Item control or a List Editor control may not be ready for customization immediately after creation. If the technique described in this topic does not have the desired effect, handle platform-specific events listed below.

ASP.NET Core Blazor
:   XAF ASP.NET Core Blazor apps do no need specialized events to customize their underlying controls. However, you must use an EventCallback-based approach instead of handling regular C# events for [underlying Blazor UI controls](xref:404767). In rare cases, you can also handle the `DevExpress.ExpressApp.Blazor.Editors.Models.DxGridModel.ComponentInstanceCaptured` event to access underlying component instance and its full API. For more information, refer to the [Handle Component Events](xref:404767#handle-component-events) section.

Windows Forms:
:   The [](xref:System.Windows.Forms.Control) object's [HandleCreated](xref:System.Windows.Forms.Control.HandleCreated), [VisibleChanged](xref:System.Windows.Forms.Control.VisibleChanged), or [ParentChanged](xref:System.Windows.Forms.Control.ParentChanged) event.

    You can also handle `Load` or any similar event if the current control type exposes it.

Contact our [Support Center](https://supportcenter.devexpress.com/ticket/list) if you need help.