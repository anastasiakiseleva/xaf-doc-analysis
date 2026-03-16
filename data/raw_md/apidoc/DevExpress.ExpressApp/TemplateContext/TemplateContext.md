---
uid: DevExpress.ExpressApp.TemplateContext
name: TemplateContext
type: Struct
summary: Represents a [Template](xref:112609) context.
syntax:
  content: 'public struct TemplateContext : IEquatable<TemplateContext>'
seealso:
- linkId: DevExpress.ExpressApp.TemplateContext._members
  altText: TemplateContext Members
- linkId: "112696"
- linkId: "112609"
---
To represent [Views](xref:112611) in a UI, **XAF** uses [Windows and Frames](xref:112608). These are abstract entities visualized in the UI via Templates - controls implementing the [](xref:DevExpress.ExpressApp.Templates.IWindowTemplate) and [](xref:DevExpress.ExpressApp.Templates.IFrameTemplate) interfaces. Templates define what a Window or a Frame will look like, what [Action Containers](xref:112610) will be present and where the View site will be located. **XAF** has a number of built-in templates which are used in different situations. For instance, there is a Template used to display the main Window and a Template used to display a pop-up Window. For a description of built-in templates, refer to the [Templates](xref:112609) help topic.

When a Frame or a Window needs to be instantiated, **XAF** must determine what Template should be used. Template contexts solve this task. They are used as parameter values by the [XafApplication.CreateFrame](xref:DevExpress.ExpressApp.XafApplication.CreateFrame(DevExpress.ExpressApp.TemplateContext)) and [XafApplication.CreateWindow](xref:DevExpress.ExpressApp.XafApplication.CreateWindow*) methods. A Template context is an instance of the **TemplateContext** structure. Instances differ only by their names exposed via the [TemplateContext.Name](xref:DevExpress.ExpressApp.TemplateContext.Name) property. All the possible contexts are predefined, and are accessible via static properties of the **TemplateContext** structure. For example, there is the nested frame context defined by the [TemplateContext.NestedFrame](xref:DevExpress.ExpressApp.TemplateContext.NestedFrame) property. When a Frame is instantiated in such a context, **XAF** will use **NestedFrameTemplateV2** as the Frame's control. Another example is the undefined context defined by the [TemplateContext.Undefined](xref:DevExpress.ExpressApp.TemplateContext.Undefined) field. When this context is used, **XAF** will try to use the most appropriate Template in a given situation.

Generally, you do not need to operate contexts, because Frames and Windows are instantiated automatically. However, you can customize existing Templates and create new ones. To learn how to do this, refer to the [Template Customization](xref:112696) help topic. This topic also contains a table, listing the Templates associated with particular contexts.