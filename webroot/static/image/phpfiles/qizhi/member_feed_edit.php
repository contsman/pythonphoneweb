<?php
/**
 * ��Ա��־�༭
 *
 * @version        $Id: member_feed_edit.php 1 14:08 2010��7��19��Z tianya $
 * @package        DedeCMS.Administrator
 * @copyright      Copyright (c) 2007 - 2010, DesDev, Inc.
 * @license        http://help.dedecms.com/usersguide/license.html
 * @link           http://www.dedecms.com
 */
require_once(dirname(__FILE__)."/config.php");
CheckPurview('sys_Log');
if(empty($dopost))
{
    ShowMsg("��ûָ���κβ�����","javascript:;");
    exit();
}
if(empty($dellog)) $dellog = 0;

//�����ѡ��־
if($dopost == "clearcheck")
{
    $nowtime = time();
    $starttime = $nowtime - (24*3600);
    $endtime =$nowtime -($dellog*24*3600);
    $dsql->ExecuteNoneQuery("DELETE FROM #@__member_feed WHERE dtime BETWEEN $endtime AND $starttime ");
    ShowMsg("�ɹ���չ�ȥ".$dellog."���¼��","member_info_main.php?type=feed");
    exit();
}
//���������־
else if($dopost == "clear")
{
    $dsql->ExecuteNoneQuery("TRUNCATE TABLE #@__member_feed");
    ShowMsg("�ɹ�������м�¼��","memberlog_list.php");
    exit();
}
//ɾ��ѡ����־
else if($dopost == "del")
{
    $bkurl = isset($_COOKIE['ENV_GOBACK_URL']) ? $_COOKIE['ENV_GOBACK_URL'] : "member_feed_main.php";
    $ids = explode('`', $ids);
    $dquery = "";
    foreach($ids as $id)
    {
        if($dquery=="") $dquery .= " fid='$id' ";
        else $dquery .= " OR fid='$id' ";
    }
    if($dquery!="") $dquery = " WHERE ".$dquery;
    $dsql->ExecuteNoneQuery("DELETE FROM #@__member_feed $dquery");
    ShowMsg("�ɹ�ɾ��ָ���ļ�¼��",$bkurl);
    exit();
}
//���ѡ����־
else if($dopost=="check")
{
    $bkurl = isset($_COOKIE['ENV_GOBACK_URL']) ? $_COOKIE['ENV_GOBACK_URL'] : "member_feed_main.php";
    $ids = explode('`', $ids);
    $dquery = "";
    foreach($ids as $id)
    {
        if($dquery=="") $dquery .= " fid='$id' ";
        else $dquery .= " OR fid='$id' ";
    }
    if($dquery!="") $dquery = " WHERE ".$dquery;
    $dsql->ExecuteNoneQuery("UPDATE #@__member_feed SET ischeck=1 $dquery");
    ShowMsg("�ɹ����ָ���ļ�¼��",$bkurl);
    exit();
} else {
    ShowMsg("�޷�ʶ���������","javascript:;");
    exit();
}