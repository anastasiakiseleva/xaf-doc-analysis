---
uid: DevExpress.ExpressApp.ApplicationBuilder.SecuredXPObjectSpaceProviderOptions.AllowICommandChannelDoWithSecurityContext
name: AllowICommandChannelDoWithSecurityContext
type: Property
summary: Allows to pass commands to database provider.
syntax:
  content: public bool AllowICommandChannelDoWithSecurityContext { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '`true` if execution of [Direct SQL Queries](xref:8914) and [Stored Procedures](xref:8919) is allowed in [Integrated Mode](xref:113436) of the [Security System](xref:113366), or when the [Middle Tier Security server](xref:113439) is used; otherwise, `false`.'
seealso: []
---

If you set this property to `true`, it indicates that you can execute [Direct SQL Queries](xref:8914) and [Stored Procedures](xref:8919) in [Integrated Mode](xref:113436) of the [Security System](xref:113366), or when the [Middle Tier Security server](xref:113439) is used.