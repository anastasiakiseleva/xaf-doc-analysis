---
uid: DevExpress.ExpressApp.Security.PermissionRequestProcessorBase`1
name: PermissionRequestProcessorBase<ProcessorPermissionRequestType>
type: Class
summary: An abstract base class for Permission Request Processors.
syntax:
  content: 'public abstract class PermissionRequestProcessorBase<ProcessorPermissionRequestType> : IPermissionRequestProcessor where ProcessorPermissionRequestType : class, IPermissionRequest'
  typeParameters:
  - id: ProcessorPermissionRequestType
    description: ''
seealso:
- linkId: DevExpress.ExpressApp.Security.PermissionRequestProcessorBase`1._members
  altText: PermissionRequestProcessorBase<ProcessorPermissionRequestType> Members
---
All Permission Requests (see [](xref:DevExpress.ExpressApp.Security.IPermissionRequest)) should have an appropriate Permission Request Processor known by the Security Strategy. To implement such a processor, inherit this class and pass the Permission Request type as the ancestor class' generic parameter. Handle the [SecurityStrategy.CustomizeRequestProcessors](xref:DevExpress.ExpressApp.Security.SecurityStrategy.CustomizeRequestProcessors) event to register your custom processor, use the event's  **Permissions** parameter to access current permissions. Refer to the [How to: Implement Custom Security Objects (Users, Roles, Operation Permissions)](xref:113384) topic to see an example.