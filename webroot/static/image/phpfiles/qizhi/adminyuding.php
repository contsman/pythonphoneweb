<?php
require_once(dirname(__FILE__)."/config.php");
//Ȩ�޼��
CheckPurview('sys_Feedback');
require_once(DEDEINC."/datalistcp.class.php");
require_once(DEDEINC."/typelink.class.php");
setcookie("ENV_GOBACK_URL",$dedeNowurl,time()+3600,"/");
if(!empty($job))
{
	$ids = ereg_replace("[^0-9,]",'',$fid);
	if(empty($ids))
	{
		ShowMsg("��ûѡ���κ�ѡ�",$_COOKIE['ENV_GOBACK_URL'],0,500);
		exit;
	}
}
else
{
	$job = '';
}

//ɾ������
if( $job == 'del' )
{
		$query = "Delete From `#@__yuding` where id in($ids) ";
		$dsql->ExecuteNoneQuery($query);
		ShowMsg("�ɹ�ɾ��ָ��������!",$_COOKIE['ENV_GOBACK_URL'],0,500);
		exit();
}


//�������
else
{
	$bgcolor = '';
	$typeid = isset($typeid) && is_numeric($typeid) ? $typeid : 0;
	if(!isset($keyword))
	{
		$keyword = '';
	}
	$tl = new TypeLink($typeid);
	$openarray = $tl->GetOptionArray($typeid,$cuserLogin->getUserChannel(),0);
	if($cuserLogin->getUserChannel()<=0)
	{
		$typeCallLimit = "";
	}
	else
	{
		$typeCallLimit = "And typeid in (".GetSonIds($cuserLogin->getUserChannel()).")";
	}
	if($typeid!=0)
	{
		$arttypesql = " And typeid in (".GetSonIds($typeid).")";
	}
	else
	{
		$arttypesql = "";
	}
	$querystring = "select * from #@__yuding  order by id desc";
	$dlist = new DataListCP();
	$dlist->pageSize = 10;
	$dlist->SetParameter("typeid",$typeid);
	$dlist->SetParameter("keyword",$keyword);
	$dlist->SetTemplate(DEDEADMIN."/templets/adminyuding.htm");
	$dlist->SetSource($querystring);
	$dlist->Display();
}
?>