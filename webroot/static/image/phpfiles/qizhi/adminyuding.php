<?php
require_once(dirname(__FILE__)."/config.php");
//权限检查
CheckPurview('sys_Feedback');
require_once(DEDEINC."/datalistcp.class.php");
require_once(DEDEINC."/typelink.class.php");
setcookie("ENV_GOBACK_URL",$dedeNowurl,time()+3600,"/");
if(!empty($job))
{
	$ids = ereg_replace("[^0-9,]",'',$fid);
	if(empty($ids))
	{
		ShowMsg("你没选中任何选项！",$_COOKIE['ENV_GOBACK_URL'],0,500);
		exit;
	}
}
else
{
	$job = '';
}

//删除评论
if( $job == 'del' )
{
		$query = "Delete From `#@__yuding` where id in($ids) ";
		$dsql->ExecuteNoneQuery($query);
		ShowMsg("成功删除指定的评论!",$_COOKIE['ENV_GOBACK_URL'],0,500);
		exit();
}


//浏览评论
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