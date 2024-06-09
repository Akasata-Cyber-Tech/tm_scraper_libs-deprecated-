class keywords:
    keyword_attacks = ('((("/var/log*") and "*ATTACK*") or (http and (dpt:(80 or 443 or 8080) or spt:(80 or 443)))) and (severity:(4 OR 5 OR 6 OR 7 OR 8 OR 9 OR 10 OR 11 OR 12 OR 13 OR 14 OR 15 OR 16) or TA0043 or TA0042 or TA0040 or TA0011 or TA0009 or TA0008 or TA0007 or TA0006 or TA0005 or TA0004 or TA0003 or TA0002 or TA0001 or filterRiskLevel:(critical or high or medium)) AND NOT (rupa2 or filePath:("/etc/nginx/cache*") or ruleName:("DNS response resolves to dead IP address" or "Possible Traffic Signaling - TCP" or "Unsuccessful logon to Kerberos" or "Possible DGA - DNS" or "Unregistered service running on non-standard port" or "Possible CONFICKER DNS Response" or "Possible CONFICKER DNS Response" or "DCE-RPC" or "Potential Threat (File was analyzed by Virtual Analyzer) - HTTP (Response)"))')
    keyword_malware = ('malName:* AND NOT malName:""')
    keyword_malware_regional2 = ('( "Regional 2" or 10.10.*.* or 10.90.*.* or 10.88*.* or 103.19.80.* or 103.19.81.* or 10.90**) and malName:* AND NOT malName:""')
    keywords_suspicious_dns_response = ('app:"DNS Response" and ruleName:(*DNS* or *Response*) and not ruleName:*IP Address*')
    keywords_dns = ('app:DNS')
    keywords_suspicious_dns_response_reg2 = ('("Regional 2" or 10.10.*.* or 10.90.*.*  or 10.88.*.* or 103.19.80.* or 103.19.81.* or 10.90**) and app:"DNS Response" and ruleName:(*DNS*  or *Response*) and not ruleName:*IP Address*')
    keyword_attacks_regional2 = ('((("/var/log*" or "/var/log/*/*") and "*ATTACK*") or (TA0043 or TA0042 or TA0040 or TA0011 or TA0009 or TA0008 or TA0007 or TA0006 or TA0005 or TA0004 or TA0003 or TA0002 or TA0001 or filterRiskLevel:(critical or high or medium))) or ((dpt:(80 or 443 or 8080) or spt:(80 or 443)) or app:http)) and (("Regional 2" or 10.10.*.* or 10.88.*.* or 103.19.80.* or 103.19.81.*) AND NOT (filePath:("/etc/nginx/cache*") or ruleName:("Web Server - Nginx" or "DNS response resolves to dead IP address" or "Possible Traffic Signaling - TCP" or "Unsuccessful logon to Kerberos" or "Possible DGA - DNS" or "Unregistered service running on non-standard port" or "Possible CONFICKER DNS Response" or "Possible CONFICKER DNS Response" or "DCE-RPC" or "Potential Threat (File was analyzed by Virtual Analyzer) - HTTP (Response)"))')
    keyword_behavior_violation = ('eventName: "BEHAVIORAL_VIOLATION"')
    keyword_logon_rdp = ('"winEventId: 4624 AND (eventDataLogonType:(10 OR 2) OR (\"*\\\"LogonType\\\" : \\\"10\\\"*\" OR \"*\\\"LogonType\\\" : \\\"2\\\"*\"))"')
    keyword_smb_logon = ('XSAE.F5920')
    
    keyword_rdp_ddi = ('SVRCCTV01 AND eventDataLogonType:(10 OR 2)')
    keyword_tacticsId = ('tacticId:(TA0043 or TA0042 or TA0040 or TA0011 or TA0009 or TA0008 or TA0007 or TA0006 or TA0005 or TA0004 or TA0003 or TA0002 or TA0001) or malName:* AND NOT malName:"" or actResult: File passed OR actResult: file OR actResult: action or filterRiskLevel: (critical OR high OR medium OR low) and eventSubId: 301')
    keyword_ddi = ('(productCode:pdi) or (productCode:(sds or sao or xes) and not filterRiskLevel:info)')
    keyword_ssh = ("eventName: \"LOG_INSPECTION_EVENT\" and not (\"10.10.32.100\" or \"10.10.35.100\") and ruleName: Auditd")
    
    keyword_monitoring_r2 = [
        keyword_attacks_regional2,
        keyword_malware_regional2,
        keywords_suspicious_dns_response_reg2,
        keyword_ssh,
        keyword_logon_rdp,
        keyword_rdp_ddi
    ]
    
    keyword_monitoring = [
        keyword_attacks,
        keyword_malware,
        keywords_dns,
        keyword_ssh,
        # keyword_logon_rdp,
        keyword_rdp_ddi,
        keyword_smb_logon]
    # keyword_monitoring = ('request:(* and not "")')
    # keyword_monitoring = ('src:(* and not "") and not dst:"" or ')
    # keyword_monitoring = ('src:(* and not "") and not dst:""')
    
    custom = ('')
    # Logon Query:

    # Attacks Query:

    # DNS Traffic Query:

    # Malware Detection Query:
    
    